# Class decorator to trace external instance attribute fetches

def Tracer(aClass):                                   # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.wrapped = aClass(*args, **kargs)     # Use enclosing scope name
        def __getattr__(self, attrname):
            print('Trace:', attrname)                 # Catches all but .wrapped
            return getattr(self.wrapped, attrname)    # Delegate to wrapped object
    return Wrapper

@Tracer
class Person:                                         # Person = Tracer(Person)
    def __init__(self, name, hours, rate):            # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                              # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)                           # bob is really a Wrapper
print(bob.name)                                       # Wrapper embeds a Person
print(bob.pay())                                      # Triggers __getattr__
