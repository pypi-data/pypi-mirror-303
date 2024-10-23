"""Image element module."""
from ..base_element import BaseElement
from RPA.HTTP import HTTP
import os


class ImageElement(BaseElement):
    """Class for image element model."""

    def downlaod_image(self, download_path: str) -> None:
        """Download images using RPA.HTTP and return the local path."""
        http = HTTP()
        url = self.get_element_attribute("src")
        filename = url.split("/")[-1].split("?")[0]  # Basic cleaning to remove URL parameters
        filepath = os.path.join(download_path, filename)
        http.download(url, filepath)
        return filepath
