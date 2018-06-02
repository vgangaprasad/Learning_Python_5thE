class InstState:                           # Using instance state, (object) in 2.X
    def __get__(self, instance, owner):
        print('InstState get')             # Assume set by client class
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

# Client class
class CalcAttrs:
    X = InstState()                        # Descriptor class attr
    Y = 3                                  # Class attr
    def __init__(self):
        self._X = 2                        # Instance attr
        self.Z  = 4                        # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X is computed, others are not
obj.X = 5                                  # X assignment is intercepted
CalcAttrs.Y = 6                            # Y reassigned in class
obj.Z = 7                                  # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                         # But X differs now, like Z!
print(obj2.X, obj2.Y, obj2.Z)
