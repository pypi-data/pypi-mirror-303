"""Classes for bug catcher."""
import datetime
import os

from .bot_config import BotConfig
from .utils.logger import logger
from t_bug_catcher import attach_file_to_exception, report_error


def attach_browser_data_if_error(func: callable) -> callable:
    """Decorator to attach browser data to exception if error occurs.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """

    def wrapper(*args, **kwargs) -> callable:
        if args:
            self = args[0]
            if isinstance(self.__class__, BugCatcherMeta):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    if hasattr(self, "browser") and BotConfig.capture_screenshot_on_error:
                        ts = datetime.datetime.now().strftime("%H_%M_%S")
                        file_name = f"{self.__class__.__name__}_{self.xpath[2:]}_{ts}.png"
                        file_path = os.path.join(BotConfig.output_folder, file_name)
                        try:
                            self.browser.capture_page_screenshot(file_path)
                            logger.info(f"Screenshot saved to {file_path}")
                            attach_file_to_exception(e, file_path)
                        except Exception as ex:
                            report_error(ex, "Failed to capture screenshot")
                            logger.warning(f"Failed to capture screenshot due to error : {str(ex)}")
                    raise
                return result

    return wrapper


class BugCatcherMeta(type):
    """Metaclass for bug catcher."""

    def __new__(cls, name: str, bases: tuple[type, ...], dct: any) -> any:
        """New method for metaclass."""
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                dct[attr_name] = attach_browser_data_if_error(attr_value)
        return super().__new__(cls, name, bases, dct)
