# File testmixin0.py
from listinstance import ListInstance # Get lister tool class

class Super:
    def __init__(self):               # Superclass __init__
        self.data1 = 'spam'           # Create instance attrs
    def ham(self):
        pass

class Sub(Super, ListInstance):       # Mix in ham and a __str__
    def __init__(self):               # Listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'           # More instance attrs
        self.data3 = 42
    def spam(self):                   # Define another method here
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                          # Run mixed-in __str__
