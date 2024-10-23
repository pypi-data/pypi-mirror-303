"""Store the classes and fixtures used throughout the tests."""

from pathlib import Path

import pytest


@pytest.fixture(name="work_dir")
def work_dir_(tmp_path: Path) -> Path:
    """Create the work directory for the tests."""
    return tmp_path
