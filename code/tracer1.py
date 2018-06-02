class tracer:
    def __init__(self, func):          # Remember original, init counter
        self.calls = 0
        self.func  = func
    def __call__(self, *args):         # On later calls: add logic, run original
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

@tracer                                # Same as spam = tracer(spam)
def spam(a, b, c):                     # Wrap spam in a decorator object
    return a + b + c

print(spam(1, 2, 3))                   # Really calls the tracer wrapper object
print(spam('a', 'b', 'c'))             # Invokes __call__ in class
