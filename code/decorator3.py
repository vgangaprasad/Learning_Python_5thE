calls = 0
def tracer(func):                         # State via enclosing scope and global
    def wrapper(*args, **kwargs):         # Instead of class attributes
        global calls                      # calls is global, not per-function
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

spam(1, 2, 3)             # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, assigned to eggs
eggs(4, y=4)              # Global calls is not per-decoration here!
