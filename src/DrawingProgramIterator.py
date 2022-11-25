
class DrawingProgramIterator:
    """
    This class represents DrawingProgram Iterator
    """
    def __init__(self, list):
        """Constructor"""
        self._index = 0
        self.list = list

    def __iter__(self):
        """Creates iterator object, called when iteration is initialized"""
        return self

    def __next__(self):
        """Method to move to next element """
        if self._index < len(self.list):
            ret = self.list[self._index]
            self._index += 1
            return ret
        else:
            raise StopIteration
