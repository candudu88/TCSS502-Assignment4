from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_name):
        self.__shape_name = shape_name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius, name_of_shape):
        super().__init__(name_of_shape)
        self.name_of_shape = None
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius

    def draw(self):
        print(f"{self.name_of_shape}, area: {self.area()}, perimeter: {self.perimeter()}")


class Square(Shape):
    def __init__(self, side, name_of_shape):
        super().__init__(name_of_shape)
        self.name_of_shape = None
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

    def draw(self):
        print(f"{self.name_of_shape}, area: {self.area()}, perimeter: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, length, width, name_of_shape):
        super().__init__(name_of_shape)
        self.name_of_shape = None
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length * 2 + self.__width * 0.5

    def draw(self):
        print(f"{self.name_of_shape}, area: {self.area()}, perimeter: {self.perimeter()}")


class Triangle(Shape):
    def __init__(self, base, height, name_of_shape):
        super().__init__(name_of_shape)
        self.name_of_shape = None
        self.__base = base
        self.__height = height

    def area(self):
        return self.__base * self.__height % 2

    def perimeter(self):
        return 4 * self.__side

    def draw(self):
        print(f"{self.name_of_shape}, area: {self.area()}, perimeter: {self.perimeter()}")
