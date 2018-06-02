# File contains_yield.py
from __future__ import print_function         # 2.X/3.X compatibility

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):                 # Fallback for iteration
        print('get[%s]:' % i, end='')         # Also for index, slice
        return self.data[i]
    def __iter__(self):                       # Preferred for iteration
        print('iter=> next:', end='')         # Allows multiple active iterators
        for x in self.data:                   # no __next__ to alias to next
            yield x
            print('next:', end='')
    def __contains__(self, x):                # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])        # Make instance
    print(3 in X)                     # Membership 
    for i in X:                       # for loops
        print(i, end=' | ')

    print()
    print([i ** 2 for i in X])        # Other iteration contexts
    print( list(map(bin, X)) )

    I = iter(X)                       # Manual iteration (what other contexts do)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
