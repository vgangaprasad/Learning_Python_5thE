# Descriptor options: A call tracer decorator for both functions and methods


class tracer(object):                        # A decorator+descriptor
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):      # On method attribute fetch
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):          # Save both instances
        self.desc = desc                     # Route calls back to deco/desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)  # Runs tracer.__call__


"""
class tracer(object):                        # More succinct: nested function
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):                # On method fetch
        def wrapper(*args, **kwargs):                  # Retain both inst
            return self(instance, *args, **kwargs)     # Runs __call__
        return wrapper
"""


"""
class tracer(object):                        # For methods, but not functions!
    def __init__(self, meth):                # On @ decorator
        self.calls = 0                         
        self.meth  = meth
    def __get__(self, instance, owner):      # On method fetch
        def wrapper(*args, **kwargs):        # On method call: proxy with self+inst
            self.calls += 1
            print('call %s to %s' % (self.calls, self.meth.__name__))
            return self.meth(instance, *args, **kwargs)
        return wrapper
"""


if __name__ == '__main__':

    # Applies to simple functions
    @tracer
    def spam(a, b, c):                       # spam = tracer(spam)
        print(a + b + c)                     # Uses __call__ only

    @tracer
    def eggs(N):
        return 2 ** N

    spam(1, 2, 3)                            # Runs onCall(1, 2, 3)
    spam(a=4, b=5, c=6)
    print(eggs(32))

    # Applies to class method functions too!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay  = pay

        @tracer
        def giveRaise(self, percent):        # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)      # Makes giveRaise a descriptor

        @tracer
        def lastName(self):                  # lastName = tracer(lastName)
            return self.name.split()[-1]

    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                       # Runs onCall(sue, .10)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())    # Runs onCall(bob), lastName in scopes
