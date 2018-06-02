class Squares:                                   # manual generator function calls
    def __init__(self, start, stop):             # __next__ is automatic/implied
        self.start = start
        self.stop  = stop
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
