from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle


class ShapeFactory:

    @staticmethod
    def create_shape(shape, *args):
        if shape == "Circle":
            return Circle(shape, args[0])
        elif shape == "Square":
            return Square(shape, args[0])
        elif shape == "Rectangle":
            return Rectangle(shape, args[0], args[1])
        elif shape == "Triangle":
            return Triangle(shape, args[0], args[1])
        else:
            raise Exception




