# 2 dynamically computed attributes with properties

class Powers(object):                              # Need (object) in 2.X only
    def __init__(self, square, cube):
        self._square = square                      # _square is the base value
        self._cube   = cube                        # square is the property name

    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25
