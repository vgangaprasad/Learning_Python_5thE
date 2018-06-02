D = {}
D = {'name': 'Bob', 'age': 40.0}
print(D)
E = {'cto': {'name': 'Bob', 'age': 40}}
print(E)
D = dict(name='Bob', age=40)
print(D)
D = dict([['name', 'Bob'], ['age', 40]])
print(D)
#D = dict(zip(keyslist, valslist))
D = dict.fromkeys(['name', 'age'])
print(D)
print(D['name'])
print(E['cto']['age'])
print('age' in D)
D.keys()
D.values()
D.items()
D.copy()
#D.update(D2)
#D.get(key, default?)
#D.pop(key, default?)
#D.setdefault(key, default?)
D.popitem()
"""
len(D)
D[key] = 42
del D[key]
list(D.keys())
D1.keys() & D2.keys()
D.viewkeys(), D.viewvalues()
"""

L = []
L = [123, 'abc', 1.23, {}]
print(L)
L = ['Bob', 40.0, ['dev', 'mgr']]
print(L)
L = list('spam')
print(L)
L = list(range(-4, 4))
print(L)
"""
L[i]
L[i][j]
L[i:j]
len(L)
L1 + L2
"""
L * 3
for x in L: print(x)
3 in L
L.append(4)
L.extend([5,6,7])
print(L)
"""
L.insert(I, X)
L.index(1)
L.count(X)
L.sort()
L.reverse()
L.copy()
L.pop(i)
L.remove(2)
del L[k]
del L[i:j]
L[i:j] = []
L[i] = 3
L[i:j] = [4,5,6]
"""
L = [x**2 for x in range(5)]
print(L)
print(list(map(ord, 'spam')))
