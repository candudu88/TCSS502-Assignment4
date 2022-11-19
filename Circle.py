from Shape import Shape


class Circle(Shape):
    def __init__(self, name_of_shape, radius):
        super().__init__(name_of_shape)
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius

    def draw(self):
        print(f"{self.__shape_name}, area: {self.area()}, perimeter: {self.perimeter()}\n")