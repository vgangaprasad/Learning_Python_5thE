# Same, but with descriptors (per-instance state)

class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers(object):                          # Need all (object) in 2.X only
    square = DescSquare()
    cube   = DescCube()
    def __init__(self, square, cube):
        self._square = square                  # "self.square = square" works too,
        self._cube   = cube                    # because it triggers desc __set__!

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25
