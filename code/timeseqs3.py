# File timeseqs3.py
"""
See how this compares to later timeit results.
Now very similar to pybench.py's timeit total, but
still not identical: adds function call per total loop,
uses prebuilt list for range instead of generator.
"""

import sys, timer                               
reps = 1000                                      # <== to match pybench (1000 inner)
repslist = list(range(reps))                     # <== differs from pybench

def forLoop():
    res = []
    for x in repslist:
        res.append(x ** 2)                       # <== to match pybench (x **2 all)
    return res

def listComp():
    return [x ** 2 for x in repslist]

def mapCall():
    return list(map((lambda x: x ** 2), repslist))          # list() in 3.X only
  # return map(((lambda x: x ** 2), repslist)

def genExpr():
    return list(x ** 2 for x in repslist)                   # list() in 2.X + 3.X

def genFunc():
    def gen():
        for x in repslist:
            yield x ** 2
    return list(gen())                                      # list() in 2.X + 3.X

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
