from DrawingProgram import DrawingProgram


class DrawingProgramIterator:
    def __init__(self):
        drawing_program = DrawingProgram()
        for shape in drawing_program.list_of_shapes:
            print(shape)
