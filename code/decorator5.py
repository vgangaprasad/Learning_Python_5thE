def tracer(func):                        # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)             # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, assigned to eggs
eggs(4, y=4)              # wrapper.calls _is_ per-decoration here
