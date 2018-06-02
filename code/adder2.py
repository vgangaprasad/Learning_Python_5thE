class Adder:
    def __init__(self, start=[]):
        self.data = start
    def __add__(self, other):              # Pass a single argument
        return self.add(other)             # The left side is in self
    def add(self, y):
        print('not implemented!')

class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        d = self.data.copy()               # Change to use self.data instead of x
        d.update(y)                        # Or "cheat" by using quicker built-ins 
        return d

x = ListAdder([1, 2, 3])
y = x + [4, 5, 6]
print(y)                                   # Prints [1, 2, 3, 4, 5, 6]

z = DictAdder(dict(name='Bob')) + {'a':1}
print(z)                                   # Prints {'name': 'Bob', 'a': 1}
