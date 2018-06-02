# File timeseqs.py
"Test the relative speed of iteration tool alternatives."

import sys, timer                                # Import timer functions
reps = 10000
repslist = list(range(reps))                     # Hoist out, list in both 2.X/3.X

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))              # Use list() here in 3.X only!
  # return map(abs, repslist)

def genExpr():
    return list(abs(x) for x in repslist)        # list() required to force results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())                           # list() required to force results

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
