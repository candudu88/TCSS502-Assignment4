from Shape import Shape


class Rectangle(Shape):
    def __init__(self, name_of_shape, length, width):
        super().__init__(name_of_shape)
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length * 2 + self.__width * 0.5

    def draw(self):
        print(str(self))

    def __str__(self):
        return f"{self.get_name()}, area: {self.area()}, perimeter: {self.perimeter()}"
