import builtins

def makeopen(id):
    original = builtins.open
    def custom(*kargs, **pargs):
        print('Custom open call %r:' % id , kargs, pargs)
        return original(*kargs, **pargs)
    builtins.open = custom
