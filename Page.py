"""Representation of a single page of text for the reader."""

from dataclasses import dataclass
from typing import List


@dataclass
class Page:
    """Container for one page of text.

    Attributes:
        number: Index of the page, starting at 0.
        lines: List of lines that make up the page.
    """

    number: int
    lines: List[str]

    def text(self) -> str:
        """Return the page content as a string."""
        return "".join(self.lines)
