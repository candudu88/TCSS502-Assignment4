from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


class DrawingProgramMain:
    drawing_program = DrawingProgram()

    # create shape to add DrawingProgram
    circle_one = ShapeFactory.create_shape("Circle", 2.0)
    circle_two = ShapeFactory.create_shape("Circle", 3.0)
    circle_three = ShapeFactory.create_shape("Circle", 1.0)
    square_one = ShapeFactory.create_shape("Square", 2.0)
    rectangle_one = ShapeFactory.create_shape("Rectangle", 2.0, 3.0)
    triangle_one = ShapeFactory.create_shape("Triangle", 2.0, 3.0, 4.0)

    drawing_program.add_shape(circle_one)
    drawing_program.add_shape(circle_two)
    drawing_program.add_shape(circle_three)
    # print all the shape drawing_program current contained
    print("<-----------print all the shape from drawing_program----------->")
    print(str(drawing_program) + "\n")

    # print all the shapes from drawing_program after sorting
    print("<-----------print all the shape drawing_program after sorting----------->")
    drawing_program.sort_shapes()
    print(str(drawing_program) + "\n")

    # print all the shape from drawing_program after added new shapes
    print("<-----------print all the shape from drawing_program after add new shape----------->")
    drawing_program.add_shape(triangle_one)
    drawing_program.add_shape(rectangle_one)
    print(str(drawing_program) + "\n")

    # print all the shapes from drawing_program after sorting
    print("<-----------print all the shape drawing_program after add new shape and sorting----------->")
    drawing_program.sort_shapes()
    print(str(drawing_program) + "\n")

    # print all the shapes after replace one shape and sorting
    print("<-----------print all the shapes after replace one shape and sorting----------->")
    drawing_program.set_shape(0, square_one)
    drawing_program.sort_shapes()
    print(str(drawing_program) + "\n")


if __name__ == "__main__":
    DrawingProgramMain()
