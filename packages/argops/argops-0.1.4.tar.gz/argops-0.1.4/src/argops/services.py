"""Define all the orchestration functionality required by the program to work.

Classes and functions that connect the different domain model objects with the adapters
and handlers to achieve the program's purpose.
"""

import contextlib
import difflib
import filecmp
import logging
import os
import re
import shutil
from io import StringIO
from pathlib import Path
from typing import List, Optional

import git
from git.exc import InvalidGitRepositoryError, NoSuchPathError
from ruyaml import YAML
from ruyaml.comments import CommentedMap

from argops.exceptions import GitRepositoryError
from argops.model import YamlDiff

log = logging.getLogger(__name__)


log = logging.getLogger(__name__)

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def promote_changes(
    src_dir: str, dest_dir: str, filters: List[str], dry_run: bool = False
) -> None:
    """Promote changes from the source directory to the destination directory.

    Args:
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.
        filters (List[str]): List of chart directory names to filter.
        dry_run (bool): If True, perform a dry run showing changes without
            copying files.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        log.info(f"Created destination directory: {dest_dir}")

    # Find all directories with a Chart.yaml file that match the chart names
    chart_directories = find_chart_directories(src_dir, filters)

    # Sync each directory
    for directory in chart_directories:
        dest_path = os.path.join(dest_dir, directory)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            log.info(f"Created destination directory: {dest_path}")

        comparison = filecmp.dircmp(
            os.path.join(src_dir, directory), os.path.join(dest_dir, directory)
        )
        sync_directory(
            comparison,
            os.path.join(src_dir, directory),
            os.path.join(dest_dir, directory),
            dry_run,
        )


def find_chart_directories(src_dir: str, filters: List[str]) -> List[str]:
    """Find directories containing a Chart.yaml file that match the chart names.

    Args:
        src_dir (str): The path to the source directory.
        filters (List[str]): List of chart directory names to filter.

    Returns:
        List[str]: List of directory paths to sync.
    """
    directories = []

    for root, _, files in os.walk(src_dir):
        if "Chart.yaml" in files:
            relative_path = os.path.relpath(root, src_dir)
            if len(filters) == 0 or os.path.basename(root) in filters:
                directories.append(relative_path)

    return directories


def sync_new_file(file_name: str, src_dir: str, dest_dir: str, dry_run: bool) -> None:
    """Handle new files and directories.

    By copying them from the source to the destination directory.

    Args:
        file_name (str): The name of the file or directory.
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    src_path = os.path.join(src_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name.replace("-staging", "-production"))

    if file_name == "values-staging.yaml":
        promote_values_files(file_name, src_dir, dest_dir, dry_run)
    elif file_name == "secrets.yaml":
        log.warning(f"Unmanaged file: {src_path}, handle it manually")
    else:
        log.info(f"{GREEN}New{RESET}: {src_path} -> {dest_path}")
        if not dry_run:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)


def sync_deleted_file(file_name: str, dest_dir: str, dry_run: bool) -> None:
    """Handle files and directories that have been deleted from the source.

    By removing them from the destination directory.

    Args:
        file_name (str): The name of the file or directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    dest_path = os.path.join(dest_dir, file_name)

    if file_name in ["values-production.yaml"]:
        return

    log.info(f"{RED}Deleting{RESET}: {dest_path}")
    if not dry_run:
        if os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
        else:
            os.remove(dest_path)


def sync_updated_file(
    file_name: str, src_dir: str, dest_dir: str, dry_run: bool
) -> None:
    """Handle updated files.

    By copying them from the source to the destination directory
    and logging differences.

    Args:
        file_name (str): The name of the file.
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    src_path = os.path.join(src_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)

    if file_name == "secrets.yaml":
        log.warning(f"Unmanaged file: {src_path}, handle it manually")
        return

    log.info(f"{YELLOW}Updating file{RESET}: {src_path} -> {dest_path}\n")
    show_file_diff(src_path, dest_path)

    if file_name == "values-staging.yaml":
        promote_values_files(file_name, src_dir, dest_dir, dry_run)
    else:
        if not dry_run:
            shutil.copy2(src_path, dest_path)


# ignore: Missing type parameters for generic type dircmp
# The standard filecmp.dircmp class from Python's standard library
# does not require or support type parameters.
def sync_directory(
    comparison: filecmp.dircmp,  # type: ignore
    src_dir: str,
    dest_dir: str,
    dry_run: bool,
) -> None:
    """Synchronize the changes between two directories.

    It performs the following operations:
    - Copy new and updated files from the source directory to the destination
      directory.
    - Delete files and directories that are not in the source directory.

    Args:
        comparison (filecmp.dircmp): The directory comparison object.
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    for file_name in comparison.left_only:
        sync_new_file(file_name, src_dir, dest_dir, dry_run)

    for file_name in comparison.right_only:
        sync_deleted_file(file_name, dest_dir, dry_run)

    for file_name in comparison.diff_files:
        sync_updated_file(file_name, src_dir, dest_dir, dry_run)

    for subdir_name in comparison.common_dirs:
        subdir_comparison = comparison.subdirs[subdir_name]
        sync_directory(
            subdir_comparison,
            os.path.join(src_dir, subdir_name),
            os.path.join(dest_dir, subdir_name),
            dry_run,
        )


def promote_values_files(
    file_name: str, src_dir: str, dest_dir: str, dry_run: bool = False
) -> None:
    """Promote changes from values-staging.yaml to values-production.yaml.

    By comparing the YAML contents.

    Args:
        file_name (str): The name of the YAML file (e.g., "values-staging.yaml").
        src_dir (str): The source directory containing the staging file.
        dest_dir (str): The destination directory containing the production file.
        dry_run (bool): If True, only show the diff without making any changes.
    """
    staging_file_path = os.path.join(src_dir, file_name)
    production_file_path = os.path.join(
        dest_dir, file_name.replace("staging", "production")
    )
    log.info(f"Promoting the changes from {staging_file_path}")

    last_promoted_commit = get_last_promoted_commit_id(production_file_path)
    last_commit = get_last_commit_id()
    log.debug(f"Last promoted commit of {staging_file_path} is {last_promoted_commit}")
    log.debug(f"Last commit is {last_commit}")

    # Get the different contents
    if not last_promoted_commit:
        last_promoted_content = ""
    else:
        last_promoted_content = get_content(staging_file_path, last_promoted_commit)

    log.debug(
        f"Creating the updated values of {production_file_path} "
        f"from the latest version of {staging_file_path}"
    )
    old_production_content = get_content(production_file_path)
    new_content = update_values(
        last_promoted_content,
        get_content(staging_file_path),
        old_production_content,
        last_commit,
    )

    if not dry_run:
        Path(production_file_path).write_text(new_content, encoding="utf8")

        log.debug(f"Promotion completed. Changes applied to {production_file_path}")


def update_values(
    last_promoted_source_content: str,
    source_content: str,
    destination_content: str,
    last_promoted_commit_id: str = "HEAD",
) -> str:
    """Updates the destination YAML content.

    By applying changes from the source content, including new, changed,
    and deleted properties. Updates the last promoted commit ID in the destination
    content.

    Args:
        last_promoted_source_content (str): The previous source YAML content.
        source_content (str): The current source YAML content.
        destination_content (str): The current destination YAML content.
        last_promoted_commit_id (str): The last promoted git commit id.

    Returns:
        str: The updated YAML content with comments.
    """
    log.debug("Comparing source contents.")
    diff = compare_yaml_contents(last_promoted_source_content, source_content)

    if not diff.has_changed:
        log.debug("The source has not changed since the last promoted commit")
        return destination_content

    # Read the current production file
    if destination_content == "":
        log.debug("Destination content is empty, initializing from the source content.")
        new_content = YAML().load(source_content)
        diff.new = diff.new + diff.unchanged + diff.changed
        diff.changed = []
        diff.deleted = []
    else:
        log.debug("Loading existing destination content.")
        new_content = YAML().load(destination_content)

    def apply_diff(
        new_content: CommentedMap, diff: YamlDiff, parent_key: Optional[str] = ""
    ) -> None:
        """Recursively applies differences to the content, handling nested structures.

        Args:
            new_content (Dict[str, Any]): The content to be updated.
            diff (Any): The difference object containing new, changed, and
                deleted items.
            parent_key (Optional[str]): The parent key path for nested structures.
                Defaults to "".
        """
        log.debug(f"Applying differences to parent key: {parent_key}")

        for key, value in diff.new:
            new_content[key] = value
            comment = "New key in source"
            new_content.yaml_add_eol_comment(
                key=key,
                comment=comment,
            )
            log.debug(
                f"Added new key '{key}' with value '{value}' at path '{parent_key}'"
            )

        for key, value in diff.changed:
            if isinstance(value, dict):
                log.debug(f"Recursively applying changes to nested key: {key}")
                string_stream = StringIO()
                YAML().dump(new_content[key], string_stream)
                source_yaml = string_stream.getvalue()
                string_stream.close()
                string_stream = StringIO()
                YAML().dump(value, string_stream)
                destination_yaml = string_stream.getvalue()
                string_stream.close()

                apply_diff(
                    new_content[key],
                    compare_yaml_contents(
                        source_yaml,
                        destination_yaml,
                    ),
                    key,
                )
            else:
                comment = f"Key changed in source to {value}"
                new_content.yaml_add_eol_comment(key=key, comment=comment)
                log.info(f"Updated key '{key}' to '{value}' at path '{parent_key}'")

        for key in diff.deleted:
            if key in new_content:
                comment = "Key deleted in source"
                new_content.yaml_add_eol_comment(key=key, comment=comment)
                log.info(f"Marked key '{key}' as deleted at path '{parent_key}'")

    apply_diff(new_content, diff)

    log.debug("Updating the last promoted commit ID.")
    new_content.yaml_set_start_comment(
        f"Last promoted commit id: {last_promoted_commit_id}"
    )

    log.debug("Finished updating values.")

    string_stream = StringIO()
    YAML().dump(new_content, string_stream)
    new_content_text = string_stream.getvalue()
    string_stream.close()

    show_diff(new_content_text, destination_content)

    return new_content_text


def get_last_commit_id(repo_path: str = ".") -> str:
    """Get the last commit ID of the Git repository at the specified path.

    Args:
        repo_path (str): The path to the Git repository.
            Defaults to the current directory.

    Returns:
        str: The last commit ID.

    Raises:
        GitRepositoryError: If there is an issue accessing the repository
            or retrieving the commit ID.
    """
    try:
        repo = git.Repo(repo_path)
        last_commit = repo.head.commit
        return last_commit.hexsha
    except InvalidGitRepositoryError as e:
        raise GitRepositoryError(f"Invalid Git repository at path: {repo_path}") from e
    except NoSuchPathError as e:
        raise GitRepositoryError(f"Path does not exist: {repo_path}") from e
    except Exception as e:
        raise GitRepositoryError(f"Error retrieving last commit ID: {e}") from e


def get_last_promoted_commit_id(file_path: str) -> Optional[str]:
    """Extract the last promoted commit ID from a values-staging.yaml file.

    Args:
        file_path (str): The path to the values-staging.yaml file.

    Returns:
        str: The last promoted commit ID or None if the line doesn't exist.
    """
    commit_id_pattern = re.compile(r"# Last promoted commit id: (\w+)")

    with contextlib.suppress(FileNotFoundError), open(
        file_path, "r", encoding="utf8"
    ) as file:
        for line in file:
            match = commit_id_pattern.match(line)
            if match:
                return match.group(1)

    return None


def get_content(file_path: str, commit_id: str = "HEAD", repo_path: str = ".") -> str:
    """Get YAML content of the file at a specific commit.

    Args:
        file_path (str): The path to the file within the repository.
        commit_id (str): The commit ID to retrieve the file from. Defaults to "HEAD".
        repo_path (str): The path to the repository. Defaults to the current directory.

    Returns:
        str: The content of the file at the specified commit,
            or an empty string if the file doesn't exist.
    """
    try:
        repo = git.Repo(repo_path)
        commit = repo.commit(commit_id)
        blob = commit.tree / file_path

        content = blob.data_stream.read().decode("utf-8")
        return content

    except KeyError as e:
        log.warning(f"The '{file_path}' at commit '{commit_id}' doesn't exist: {e}")

    except Exception as e:  # noqa: W0718
        # W0718: Catching too general exception Exception. But it's what we want
        log.error(
            f"Error retrieving content for '{file_path}' at commit '{commit_id}': {e}"
        )
    return ""


def compare_yaml_contents(yaml_content_1: str, yaml_content_2: str) -> YamlDiff:
    """Compare the YAML contents from two plain text YAML strings.

    Args:
        yaml_content_1 (str): The plain text content of the first YAML.
        yaml_content_2 (str): The plain text content of the second YAML.

    Returns:
        YamlDiff: The differences between the two YAML contents.
    """
    content_1 = YAML().load(yaml_content_1)
    content_2 = YAML().load(yaml_content_2)

    # Initialize the YamlDiff object
    diff = YamlDiff()

    if not content_1:
        diff.new = [(key, content_2[key]) for key in content_2.keys()]
    elif not content_2:
        diff.deleted = content_1.keys()
    else:
        # Compare the contents
        all_keys = set(content_1.keys()).union(set(content_2.keys()))
        for key in all_keys:
            if key not in content_1:
                diff.new.append((key, content_2[key]))
            elif key not in content_2:
                diff.deleted.append(key)
            else:
                if content_1[key] != content_2[key]:
                    diff.changed.append((key, content_2[key]))
                else:
                    # E1101: Instance of FiledInfo has no append member, but it does
                    # https://github.com/pylint-dev/pylint/issues/4899
                    diff.unchanged.append((key, content_1[key]))  # noqa: E1101

    return diff


def show_diff(src: str, dest: str) -> None:
    """Show the differences between two strings.

    Args:
        src (str): The source text.
        dest (str): The destination text.
    """
    diff = difflib.unified_diff(dest.splitlines(), src.splitlines())
    for line in diff:
        printeable_line = line.rstrip("\n")
        if line.startswith("+++"):
            printeable_line = "+++ New"
        elif line.startswith("---"):
            printeable_line = "--- Old"
        if line.startswith("+"):
            log.info(f"{GREEN}{printeable_line}{RESET}")
        elif line.startswith("-"):
            log.info(f"{RED}{printeable_line}{RESET}")
        else:
            log.info(printeable_line)


def show_file_diff(src_file: str, dest_file: str) -> None:
    """Show the differences between two files.

    Args:
        src_file (str): The path to the first file.
        dest_file (str): The path to the second file.
    """
    show_diff(
        Path(src_file).read_text(encoding="utf8"),
        Path(dest_file).read_text(encoding="utf8"),
    )
