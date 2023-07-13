from typing import List

from src.models.car import Car


class Environment:
    """
    A class used to represent the environment,
    with its cars and representative data.
    """
    def __init__(self):
        self.cars: List[Car] = []
