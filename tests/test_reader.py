"""Unit tests for the Reader class."""

import json
from pathlib import Path

import pytest
import os
import sys

sys.path.append(os.getcwd())

from Reader import Reader


def make_sample_file(tmp_path: Path, lines: int = 20) -> Path:
    """Create a sample text file with numbered lines."""
    content = "\n".join(f"line {i}" for i in range(lines))
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content)
    return file_path


def test_split_into_pages(tmp_path: Path) -> None:
    file_path = make_sample_file(tmp_path, lines=10)
    state = tmp_path / "state.json"
    reader = Reader(str(file_path), page_size=4, state_file=str(state))
    assert len(reader.pages) == 3
    assert reader.pages[0].lines[0].startswith("line 0")


def test_last_read_position(tmp_path: Path) -> None:
    file_path = make_sample_file(tmp_path, lines=15)
    state = tmp_path / "state.json"
    reader = Reader(str(file_path), page_size=5, state_file=str(state))
    reader.read()  # advance one page
    new_reader = Reader(str(file_path), page_size=5, state_file=str(state))
    assert new_reader.current_page == 1


def test_reset_position(tmp_path: Path) -> None:
    file_path = make_sample_file(tmp_path, lines=15)
    state = tmp_path / "state.json"
    reader = Reader(str(file_path), page_size=5, state_file=str(state))
    reader.read()
    reader.reset()
    with open(state, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    assert data[str(file_path)] == 0

