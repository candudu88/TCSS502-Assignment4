from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle

class ShapeFactory:

    @staticmethod
    def create_shape(self, shape, parameter):
        if shape == "Circle":
            return Circle(parameter, shape)
        elif shape == "Square":
            return Square(parameter, shape)
        else:
            raise Exception

    @staticmethod
    def create_shape(self, shape, para1, para2):
        if shape == "Rectangle":
            return Rectangle(para1, para2, shape)
        elif shape == "Triangle":
            return Triangle(para1, para2, shape)
        else:
            raise Exception

