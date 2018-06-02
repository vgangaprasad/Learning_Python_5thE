class DescSquare:
    def __init__(self, start):                  # Each desc has own state
        self.value = start
    def __get__(self, instance, owner):         # On attr fetch
        return self.value ** 2
    def __set__(self, instance, value):         # On attr assign
        self.value = value                      # No delete or docs

class Client1:
    X = DescSquare(3)          # Assign descriptor instance to class attr

class Client2:
    X = DescSquare(32)         # Another instance in another client class
                               # Could also code 2 instances in same class
c1 = Client1()
c2 = Client2()

print(c1.X)                    # 3 ** 2
c1.X = 4
print(c1.X)                    # 4 ** 2
print(c2.X)                    # 32 ** 2 (1024)
