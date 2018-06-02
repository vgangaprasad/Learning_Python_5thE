from mylist import MyList

class MyListSub(MyList):
    calls = 0                                      # Shared by instances
    def __init__(self, start):
        self.adds = 0                              # Varies in each instance
        MyList.__init__(self, start)

    def __add__(self, other):
        print('add: ' + str(other))
        MyListSub.calls += 1                       # Class-wide counter
        self.adds += 1                             # Per-instance counts
        return MyList.__add__(self, other)

    def stats(self):
        return self.calls, self.adds               # All adds, my adds

if __name__ == '__main__':
    x = MyListSub('spam')
    y = MyListSub('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bar'])
    print(x.stats())
