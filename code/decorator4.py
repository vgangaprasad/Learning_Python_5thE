def tracer(func):                        # State via enclosing scope and nonlocal
    calls = 0                            # Instead of class attrs or global
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)             # Really calls wrapper, bound to func
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, bound to eggs
eggs(4, y=4)              # Nonlocal calls _is_ per-decoration here
