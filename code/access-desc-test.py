"""
File: access-test.py
Test code: separate file to allow decorator reuse.
"""
import sys
from access_desc import Private, Public

print('---------------------------------------------------------')
# Test 1: names are public if not pivate

@Private('age')                             # Person = Private('age')(Person)
class Person:                               # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age  = age                     # Inside accesses run normally
    def __add__(self, N):
        self.age += N                       # Bultins caught by mix-in in 3.X
    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('Bob', 40)
print(X.name)                               # Outside accesses validated
X.name = 'Sue'
print(X.name)
X + 10
print(X)

try:    t = X.age                           # FAILS unless "python -O"
except: print(sys.exc_info()[1])
try:    X.age = 999                         # ditto
except: print(sys.exc_info()[1])

print('---------------------------------------------------------')
# Test 2: names are private if not public
# Operators must be non-Private or Public in BuiltinMixin used

@Public('name', '__add__', '__str__', '__coerce__')  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def __add__(self, N):
        self.age += N                       # Bultins caught by mix-in in 3.X
    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('bob', 40)                       # X is an onInstance
print(X.name)                               # onInstance embeds Person
X.name = 'sue'
print(X.name)
X + 10
print(X)

try:    t = X.age                           # FAILS unless "python -O"
except: print(sys.exc_info()[1])
try:    X.age = 999                         # ditto
except: print(sys.exc_info()[1])



# more builtins tests 

@Private('age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def __add__(self, N):
        self.age += N                       # Bultins caught by mix-in in 3.X
    def __str__(self):
        return '%s: %s' % (self.name, self.age)
    def __call__(self, N):
        return self.name * N
    def __getitem__(self, I):
        return self.name[I]

X = Person('bob', 40)                       # X is an onInstance
print(X.name)                               # onInstance embeds Person
X.name = 'sue'
print(X.name)

X + 10                 # __add__

print(X)               # __str__
print(str(X))

print(X(2), X(3))      # __call__
print(X[0], X[1:])     # __getitem__
