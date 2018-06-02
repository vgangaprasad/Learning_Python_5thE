# File squares_nonyield.py

class Squares:
    def __init__(self, start, stop):                 # Non-yield generator 
        self.start = start                           # Multi scans: extra object
        self.stop  = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop  = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
