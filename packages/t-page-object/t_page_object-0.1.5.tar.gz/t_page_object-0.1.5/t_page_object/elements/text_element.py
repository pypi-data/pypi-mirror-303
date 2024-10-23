"""This module contains the TextElement class for the text element model."""
from ..base_element import BaseElement


class TextElement(BaseElement):
    """Class for input element model."""

    def get_clean_text(self):
        """Get text and clean from element."""
        text = self.get_text().strip().lower()
        return text
