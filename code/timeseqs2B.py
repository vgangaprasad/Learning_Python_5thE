# File timeseqs2.py
"""
See the effect of function call in all.
"""

import sys, timer                                # Import timer functions
reps = 10000
repslist = list(range(reps))                     # Hoist out, list in both 2.X/3.X

#...

def F(x): return x

def forLoop():
    res = []
    for x in repslist:
        res.append(F(x))
    return res

def listComp():
    return [F(x) for x in repslist]

def mapCall():
    return list(map(F, repslist))                           # list in 3.X only
  # return map(F, repslist)

def genExpr():
    return list(F(x) for x in repslist)                     # list in 2.X + 3.X

def genFunc():
    def gen():
        for x in repslist:
            yield F(x)
    return list(gen())

#...

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
