"""Contains the BasePage class which is the parent class for all page objects in the project."""
import copy
import datetime
from abc import ABC
from typing import Any
from selenium.webdriver.remote.webelement import WebElement
from SeleniumLibrary.errors import ElementNotFound
from .selenium_manager import SeleniumManager


class BasePage(ABC):
    """Base page class for all page objects in the project."""

    browser = None
    url = None
    verification_element = "//div"

    def __init__(self):
        """Base Page."""
        # Get the Selenium instance based on the portal name (if provided)
        self.browser = SeleniumManager.get_instance()

    def __deepcopy__(self, memo: Any):
        """Custom deepcopy to avoid copying the Selenium browser instance."""
        new_copy = copy.copy(self)  # Perform shallow copy
        new_copy.browser = self.browser  # Prevent deep copying the Selenium instance
        return new_copy

    def visit(self) -> None:
        """Navigate to the base page URL."""
        self.browser.go_to(self.url)
        self.wait_page_load()

    def wait_page_load(self) -> None:
        """Wait for the page to load by waiting for the verification element to load."""
        self.verification_element.wait_element_load()

    def wait_for_new_window_and_switch(self, old_window_handles: list) -> None:
        """Function for waiting and switching to new window."""
        timeout = datetime.datetime.now() + datetime.timedelta(seconds=30)
        while datetime.datetime.now() < timeout:
            currents_window_handles = self.browser.get_window_handles()
            if len(currents_window_handles) > len(old_window_handles):
                window = [window for window in currents_window_handles if window not in old_window_handles][0]
                return self.browser.switch_window(window)
        else:
            raise TimeoutError("New window was not opened")

    def get_element_from_shadow_roots(self, *roots, element_css: str) -> WebElement:
        """Get element from nested shadow roots.

        roots: The css locators of the shadow root elements.
        element_css: The css locator of the element to find.
        """
        javascript_code = (
            "return document"
            + "".join([f".querySelector('{x}').shadowRoot" for x in roots])
            + f".querySelector('{element_css}')"
        )
        element = self.browser.execute_javascript(javascript_code)
        if not isinstance(element, WebElement):
            raise ElementNotFound(f"Element not found in shadow root: {element_css}")
        return element
