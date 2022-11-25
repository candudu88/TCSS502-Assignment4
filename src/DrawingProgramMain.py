from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


class DrawingProgramMain:
    drawing_program = DrawingProgram()
    circle_one = ShapeFactory.create_shape("Circle", 2.0)
    circle_two = ShapeFactory.create_shape("Circle", 3.0)
    circle_three = ShapeFactory.create_shape("Circle", 1.0)
    drawing_program.add_shape(circle_one)
    drawing_program.add_shape(circle_two)
    drawing_program.add_shape(circle_three)
    drawing_program.sort_shapes()
    for shape in drawing_program:
        print(shape)
    print("after set new shape")
    square_one = ShapeFactory.create_shape("square", 5)
    drawing_program.set_shape(2,square_one)
    # drawing_program.add_shape(square_one)

    print(drawing_program.remove_shape("circle_three"))
    for shape in drawing_program:
        print(shape)
    # print(drawing_program.get_shape(2))


if __name__ == "__main__":
    DrawingProgramMain()