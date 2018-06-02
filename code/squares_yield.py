# File squares_yield.py

class Squares:                                   # __iter__ + yield generator
    def __init__(self, start, stop):             # __next__ is automatic/implied
        self.start = start
        self.stop  = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
