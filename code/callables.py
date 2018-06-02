class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

x = Number(2)                                       # Class instance objects
y = Number(3)                                       # State + methods
z = Number(4)
print(x.double())                                          # Normal immediate calls


acts = [x.double, y.double, y.triple, z.double]     # List of bound methods
for act in acts:                                    # Calls are deferred
    print(act())                                    # Call as though functions

bound = x.double
print(bound.__self__, bound.__func__)

print(bound.__self__.base)
print(bound())                             # Calls bound.__func__(bound.__self__, ...)

def square(arg):
    return arg ** 2                          # Simple functions (def or lambda)

class Sum:
    def __init__(self, val):                 # Callable instances
        self.val = val
    def __call__(self, arg):

        return self.val + arg

class Product:
    def __init__(self, val):                 # Bound methods
        self.val = val
    def method(self, arg):
        return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]  # Function, instance, method
for act in actions:                          # All 3 called same way
    print(act(5))                            # Call any 1-arg callable

print(actions[-1](5))                               # Index, comprehensions, maps

print([act(5) for act in actions])

print(list(map(lambda act: act(5), actions)))

class Negate:
    def __init__(self, val):                 # Classes are callables too
        self.val = -val                      # But called for object, not work
    def __repr__(self):                      # Instance print format
        return str(self.val)

actions = [square, sobject, pobject.method, Negate]     # Call a class too
for act in actions:
    print(act(5))

print([act(5) for act in actions])                     # Runs __repr__ not __str__!

table = {act(5): act for act in actions}        # 3.0 dict comprehension
for (key, value) in table.items():
    print('{0:2} => {1}'.format(key, value))    # 2.6/3.0 str.format
