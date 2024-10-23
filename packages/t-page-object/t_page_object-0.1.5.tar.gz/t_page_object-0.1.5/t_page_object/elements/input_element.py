"""Module for InputElement class."""
import time

from ..base_element import BaseElement, capture_screenshot_if_error


class InputElement(BaseElement):
    """Class for input element model."""

    @capture_screenshot_if_error
    def input_text_and_check(self, text: str, tries: int = 5) -> None:
        """
        Inputs the given text into an element and verifies the input.

        Args:
            text (str): The text to input into the element.
            tries (int, optional): The number of attempts to verify the text input. Defaults to 5.

        Returns:
            None
        """
        self.click_element_when_visible()
        self.input_text(text)
        for _ in range(tries):
            if self.get_element_attribute("value") == text:
                return
            time.sleep(1)
        raise AssertionError(f"Text '{text}' was not inputted in the input field.")

    def get_input_value(self) -> str:
        """Get input value."""
        value = self.find_element().get_attribute("value")
        return value

    def click_and_input_text(self, text: str, clear: bool = True) -> None:
        """Input text into element."""
        self.click_element_when_visible()
        self.input_text(text, clear=clear)
