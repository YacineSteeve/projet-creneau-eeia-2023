from src.utils.non_negative import non_negative


class Car:
    """
    A class used to represent any car, with its length and width.
    """

    def __init__(self, name: str = "Car EEIA 2023"):
        self.name: str = name
        self.__length: int = 0
        self.__width: int = 0

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, value: int) -> None:
        self.__length = non_negative(value, "Length")

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        self.__width = non_negative(value, "Width")

    def __str__(self) -> str:
        return f"{self.name}"
