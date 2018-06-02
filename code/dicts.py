def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]          # Or D.copy() today
    return new

def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]           # Or D1.update(D2) today
    for key in d2.keys():
        new[key] = d2[key]
    return new


"""
% python
>>> from dicts import *
>>> d = {1: 1, 2: 2}
>>> e = copyDict(d)
>>> d[2] = '?'
>>> d
{1: 1, 2: '?'}
>>> e
{1: 1, 2: 2}

>>> x = {1: 1}
>>> y = {2: 2}
>>> z = addDict(x, y)
>>> z
{1: 1, 2: 2}
"""