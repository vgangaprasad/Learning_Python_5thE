# File slots-test.py
from __future__ import print_function
import timeit
base = """
Is = []
for i in range(1000):
    X = C()
    X.a = 1; X.b = 2; X.c = 3; X.d = 4
    t = X.a + X.b + X.c + X.d  
    Is.append(X)
"""

stmt = """
class C:
    __slots__ = ['a', 'b', 'c', 'd']
""" + base
print('Slots   =>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))

stmt = """
class C:
    pass
""" + base
print('Nonslots=>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))



