import builtins

class makeopen:
    def __init__(self, id):                    # See Part 6: __call__ catches self()
        self.id = id
        self.original = builtins.open
        builtins.open = self
    def __call__(self, *kargs, **pargs):
        print('Custom open call %r:' % self.id, kargs, pargs)
        return self.original(*kargs, **pargs)
