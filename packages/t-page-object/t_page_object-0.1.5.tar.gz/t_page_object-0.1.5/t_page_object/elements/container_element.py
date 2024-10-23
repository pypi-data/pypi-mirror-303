"""Class for container elements, used to retrieve text values from div or block."""
from .text_element import TextElement
from t_object import ThoughtfulObject
from typing import Type, TypeVar

TO = TypeVar("TO", bound=ThoughtfulObject)


class ContainerElement:
    """Class for container elements."""

    def __init__(self, *args: list[TextElement]) -> None:
        """
        Initializes a container element with list of text elements.

        Args:
            *args (list[TextElement]): List of text elements

        """
        self.elements: list[TextElement] = args

    def get_text_values(self, cls: Type[TO]) -> Type[TO]:
        """
        Get text for each element with id matching class attribute.

        Args:
            cls (Type[TO]): The class to use for the object.

        Returns:
            Instance of input class with text values.
        """
        kwargs = {}
        for k, _ in cls.__annotations__.items():
            for element in self.elements:
                if element.id == k:
                    text = element.get_text()
                    kwargs[k] = "" if not text else text
        return cls(**kwargs)
