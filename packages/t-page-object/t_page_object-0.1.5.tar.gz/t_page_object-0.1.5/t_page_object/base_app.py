"""Module for BaseApp class."""
from selenium import webdriver
from pathlib import Path


class BaseApp:
    """Base class for application objects and configuration."""

    browser = None
    headless: bool = False
    wait_time: int = 10
    download_directory: str = Path().cwd() / "temp"
    browser_options: list = ["--no-sandbox", "--disable-dev-shm-usage"]
    experimental_options: dict = {
        "excludeSwitches": ["enable-automation"],
        "useAutomationExtension": False,
    }
    user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0.0.0 Safari/537.36"
    )

    def open_browser(self) -> None:
        """Open browser and set Selenium options."""
        browser_options = webdriver.ChromeOptions()

        for option in self.browser_options:
            browser_options.add_argument(option)

        for key, value in self.experimental_options.items():
            browser_options.add_experimental_option(key, value)

        if self.headless:
            browser_options.add_argument("--headless")

        self.browser.set_selenium_implicit_wait(self.wait_time)
        self.browser.set_download_directory(self.download_directory)
        self.browser.open_available_browser(user_agent=self.user_agent, options=browser_options, maximized=True)
