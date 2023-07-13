from typing import List

from src.models.car import Car


class Environment:
    def __init__(self):
        self.cars: List[Car] = []
