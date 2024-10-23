"""Define the command line interface."""

import logging
from typing import List, Optional

import typer

from .. import services
from . import utils

log = logging.getLogger(__name__)
cli = typer.Typer()


@cli.command()
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(  # noqa: W0613, M511, B008
        None, "--version", callback=utils.version_callback, is_eager=True
    ),
    src_dir: str = typer.Option("staging", "--src-dir", "-s", help="Source directory"),
    dest_dir: str = typer.Option(
        "production",
        "--dest-dir",
        "-d",
        help="Destination directory",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help=(
            "Perform a dry run, showing the differences without changing the "
            "files or directories"
        ),
    ),
    filters: List[str] = typer.Argument(
        None, help="List of applications or charts to filter"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Promote argo application between environments."""
    filters = filters or []
    ctx.ensure_object(dict)
    utils.load_logger(verbose)
    services.promote_changes(src_dir, dest_dir, filters, dry_run)


if __name__ == "__main__":
    cli()
