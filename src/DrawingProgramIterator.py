
class DrawingProgramIterator:
    """
    This class represents DrawingProgram Iterator
    """
    def __init__(self, list_of_shapes):
        """Constructor"""
        self._index = 0
        self.list_of_shapes = list_of_shapes

    def __iter__(self):
        """Creates iterator object, called when iteration is initialized"""
        return self

    def __next__(self):
        """Method to move to next element """
        if self._index < len(self.list):
            ret = self.list_of_shapes[self._index]
            self._index += 1
            return ret
        else:
            raise StopIteration
