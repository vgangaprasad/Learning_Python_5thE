"""
File timerdeco.py (3.X + 2.X)
Call timer decorator for both functions and methods.
"""
import time

def timer(label='', trace=True):             # On decorator args: retain args
    def onDecorator(func):                   # On @: retain decorated func
        def onCall(*args, **kargs):          # On calls: call original
            start   = time.clock()           # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator
