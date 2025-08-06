"""Utilities for reading text files page by page.

The :class:`Reader` class loads a text file, splits it into pages and
remembers the last read page for each file using a JSON state file.
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field
from typing import List

try:  # pragma: no cover - optional dependency
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover
    def load_dotenv() -> None:
        """Fallback no-op if python-dotenv is not installed."""
        pass

from Page import Page

load_dotenv()

STATE_FILE = os.getenv("STATE_FILE", "last_read.json")
DEFAULT_PAGE_SIZE = int(os.getenv("PAGE_SIZE", 25))


@dataclass
class Reader:
    """Manage reading state for a text file.

    Args:
        file_path: Path to the text file to read.
        page_size: Number of lines per page.
        state_file: JSON file used to store last read positions for files.
    """

    file_path: str
    page_size: int = DEFAULT_PAGE_SIZE
    state_file: str = STATE_FILE
    pages: List[Page] = field(init=False, default_factory=list)
    current_page: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        """Load the file and last read position."""
        self._load_pages()
        self.current_page = self._load_position()
        logging.debug("Starting on page %s", self.current_page)

    # Page loading -------------------------------------------------
    def _load_pages(self) -> None:
        """Read the file and split it into :class:`Page` objects."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as fh:
                lines = fh.readlines()
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"File '{self.file_path}' not found") from exc

        total_pages = (len(lines) + self.page_size - 1) // self.page_size
        self.pages = [
            Page(number=i, lines=lines[i * self.page_size:(i + 1) * self.page_size])
            for i in range(total_pages)
        ]
        logging.debug("Loaded %s pages from %s", total_pages, self.file_path)

    # Position management ------------------------------------------
    def _load_position(self) -> int:
        """Return the stored page number for this file."""
        if not os.path.exists(self.state_file):
            return 0
        with open(self.state_file, "r", encoding="utf-8") as fh:
            try:
                data = json.load(fh)
            except json.JSONDecodeError:
                logging.warning("State file corrupted; starting from page 0")
                return 0
        return data.get(self.file_path, 0)

    def _save_position(self) -> None:
        """Persist the current page number to the state file.

        The state file stores a JSON mapping of file paths to the next page
        number to read. This allows multiple books to maintain independent
        positions.
        """
        if os.path.exists(self.state_file):
            with open(self.state_file, "r", encoding="utf-8") as fh:
                try:
                    data = json.load(fh)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        data[self.file_path] = self.current_page
        with open(self.state_file, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        logging.debug("Saved page %s for %s", self.current_page, self.file_path)

    # Public API ---------------------------------------------------
    def goto(self, page_number: int) -> None:
        """Move to ``page_number``.

        Args:
            page_number: Page index to jump to.
        """
        if page_number < 0 or page_number >= len(self.pages):
            raise ValueError("Page number out of range")
        self.current_page = page_number
        logging.debug("Goto page %s", page_number)

    def reset(self) -> None:
        """Reset stored reading position to the beginning."""
        self.current_page = 0
        self._save_position()
        logging.info("Reset reading position for %s", self.file_path)

    def read(self) -> str:
        """Return the text of the current page and advance.

        Returns:
            The text content of the current page.
        """
        if not self.pages:
            return ""
        page = self.pages[self.current_page]
        # store next page as current
        self.current_page = min(self.current_page + 1, len(self.pages) - 1)
        self._save_position()
        return page.text()

