from Shape import Shape


class Triangle(Shape):
    def __init__(self, base, height, name_of_shape):
        super().__init__(name_of_shape)
        self.__side = None
        self.__base = base
        self.__height = height

    def area(self):
        return self.__base * self.__height % 2

    def perimeter(self):
        return 4 * self.__side

    def draw(self):
        print(f"{self.__shape_name}, area: {self.area()}, perimeter: {self.perimeter()}")
