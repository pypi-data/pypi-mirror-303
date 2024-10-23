"""Frame element module."""
from ..base_element import BaseElement


class IFrameElement(BaseElement):
    """Class for frame element model."""

    def select_iframe(self) -> None:
        """Select frame."""
        self.select_frame()
