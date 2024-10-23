"""Dropdown element module."""
from ..base_element import BaseElement


class DropdownElement(BaseElement):
    """Class for dropdown element model."""

    def type_and_enter(self, *text_to_enter) -> None:
        """
        Selects an option from the dropdown list based on the provided text.

        The text is input into the dropdown list input and the Enter key is pressed to select the option.

        Args:
            text_to_enter (str): The text/s of the option to be selected from the dropdown list.

        Returns:
            None
        """
        text_to_enter = list(text_to_enter)
        for text in text_to_enter:
            self.input_text(text)
            self.press_key(r"\13")

    def click_and_select_option(self, text_to_find: str, option_tag: str = "li") -> None:
        """
        Selects an option from the dropdown list based on the provided text.

        The dropdown list is clicked to open the list and the option is selected.

        Args:
            text_to_find (str): The text of the option to be selected from the dropdown list.
            option_tag (str, optional): The tag of the option to be selected from the dropdown list. Defaults to 'li'.

        Returns:
            None
        """
        self.click_element_when_visible()
        self.browser.get_webelement(f"/{option_tag}[text()='{text_to_find}']", parent=self.xpath).click()
