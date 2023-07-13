from src.utils.non_negative import non_negative


class Speed:
    def __init__(self, x: int, y: int):
        self.__x: int = non_negative(x, "Speed.x")
        self.__y: int = non_negative(y, "Speed.y")

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        self.__x = non_negative(value, "Speed.x")

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value) -> None:
        self.__y = non_negative(value, "Speed.y")
