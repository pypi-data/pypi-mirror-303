"""Congifuration module for the t_page_object package."""
from pathlib import Path


class BotConfig:
    """Class for configuration."""

    output_folder = Path().cwd() / "output"
    dev_safe_mode = True
    capture_screenshot_on_error = True

    @classmethod
    def configure(cls, **kwargs):
        """Set configuration variables."""
        for key, value in kwargs.items():
            if hasattr(cls, key):
                setattr(cls, key, value)
            else:
                raise AttributeError(f"Invalid configuration option: {key}")
