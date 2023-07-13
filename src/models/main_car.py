from src.utils.non_negative import non_negative

from .car import Car
from .speed import Speed


class MainCar(Car):
    """
    The car that will be moved
    """

    def __init__(self, name: str = "Main Car"):
        super().__init__(name)
        self.__speed: Speed = Speed(0, 0)
        self.__angle: int = 0
        self.__front_wheel_distance_to_front: int = 0
        self.__back_wheel_distance_to_back: int = 0

    @property
    def speed(self) -> Speed:
        return self.__speed

    @speed.setter
    def speed(self, value: Speed) -> None:
        self.__speed.x, self.__speed.y = value.x, value.y

    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, value: int) -> None:
        self.__angle = value

    @property
    def front_wheel_distance_to_front(self) -> int:
        return self.__front_wheel_distance_to_front

    @front_wheel_distance_to_front.setter
    def front_wheel_distance_to_front(self, distance: int) -> None:
        self.__front_wheel_distance_to_front = non_negative(distance, "Front wheel distance to front")

    @property
    def back_wheel_distance_to_back(self) -> int:
        return self.__back_wheel_distance_to_back

    @back_wheel_distance_to_back.setter
    def back_wheel_distance_to_back(self, distance: int) -> None:
        self.__back_wheel_distance_to_back = non_negative(distance, "Back wheel distance to back")

    def accelerate_x(self, speed_x: int) -> None:
        self.speed.x += speed_x

    def accelerate_y(self, speed_y: int) -> None:
        self.speed.x -= speed_y

    def accelerate(self, speed: Speed) -> None:
        self.accelerate_x(speed.x)
        self.accelerate_y(speed.y)

    def decelerate_x(self, speed_x: int) -> None:
        self.accelerate_x(-speed_x)

    def decelerate_y(self, speed_y: int) -> None:
        self.accelerate_y(-speed_y)

    def decelerate(self, speed: Speed) -> None:
        self.accelerate(Speed(-speed.x, -speed.y))

    def turn_left(self, angle: int) -> int:
        self.angle -= angle
        return self.angle

    def turn_right(self, angle: int) -> int:
        self.angle += angle
        return self.angle

    def rotate(self, angle: int) -> int:
        self.angle += angle
        return self.angle

    def __str__(self):
        return f"{self.name} " \
               f"(current speed: [ {self.speed.x}, {self.speed.y} ], " \
               f"current angle: {self.angle}°)"
