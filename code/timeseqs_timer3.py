# File timeseqs_timer2.py
"Test the relative speed of iteration tool alternatives: timer2 version"

import sys, timer3                               # <==differs
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
    return list(map(abs, repslist))              # Use list here in 3.0 only!
  # return map(abs, repslist)

def genExpr():
    return list(abs(x) for x in repslist)        # list required to force results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())                           # list required to force results

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer3.bestoftotal(test, _reps1=5, _reps=1000)
# Or:
#   (total, result) = timer3.bestoftotal(test)
#   (total, result) = timer3.bestof(test, _reps=5)  
#   (total, result) = timer3.total(test, _reps=1000)  
#   (bestof, (total, result)) = timer3.bestof(timer2.total, test, _reps=5)  

    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, total, result[0], result[-1]))
