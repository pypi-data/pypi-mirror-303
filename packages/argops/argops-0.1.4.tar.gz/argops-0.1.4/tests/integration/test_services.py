"""Integration tests of the services."""

import os
from pathlib import Path

import git

from argops.services import promote_values_files


class TestPromoteValuesFiles:
    def test_promote_values_files_production_file_updated(self, tmp_path: Path) -> None:
        file_name = "values-staging.yaml"
        src_dir = tmp_path / "staging"
        dest_dir = tmp_path / "production"
        src_dir.mkdir()
        dest_dir.mkdir()
        staging_file = src_dir / file_name
        production_file = dest_dir / file_name.replace("staging", "production")
        staging_file.write_text("foo: bar", encoding="utf8")
        repo = git.Repo.init(tmp_path)
        repo.index.add(["staging"])
        repo.index.commit("Initial commit")
        os.chdir(tmp_path)

        promote_values_files(
            "values-staging.yaml", "staging", "production", dry_run=False
        )  # act

        result_content = production_file.read_text(encoding="utf8")
        assert "\nfoo: bar  # New key in source\n" in result_content
