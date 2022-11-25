from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_name):
        self.__shape_name = shape_name

    def get_name(self):
        return self.__shape_name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass












