def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1])        # Recursive: 10x slower in CPython today

def rev2(S):
    return ''.join(reversed(S))            # Nonrecursive iterable: simpler, faster
        
def rev3(S):
    return S[::-1]                         # Even better?: sequence reversal by slice        

        
"""
>>> from reversals import *
>>> from timeit import repeat
>>> for func in (rev1, rev2, rev3):           # Beware 1k recursion depth limit!
...     print('%.10f' %
...            min(repeat(stmt=lambda: func('spam' * 200), number=20, repeat=3)))
...
0.0112213924
0.0004075886
0.0000361649
"""