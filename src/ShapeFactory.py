from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


class ShapeFactory:
    """
    This class represents an shape factory.  has create_shape method to create shape instance
    accordingly
    """
    @staticmethod
    def create_shape(shape, *args):
        """
        Creates a specific shape object based on the shape argument and raises an error if the specific shape_type of shape
        has not supported.
        :param shape: shape type to created
        :param args: allow pass multiple arguments for shape create method
        :return: specific shape instance
        """
        if shape.lower() == "circle":
            return Circle(*args)
        elif shape.lower() == "square" or (shape == "rectangle" and len(args) == 1):
            return Square(*args)
        elif shape.lower() == "rectangle":
            return Rectangle(*args)
        elif shape.lower() == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f'Shape type: {shape} not supported')




