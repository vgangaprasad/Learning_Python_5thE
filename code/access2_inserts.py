"""
Class insertion alternative: retains original class type,
but won't validate built-in operations, disallows class's own
methods to access privates, requires new-style clients in 
2.X, and breaks clients already usiing methods inserted.
"""

traceMe = True
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)

        def setattributes(self, attr, value):
            trace('set:', attr)
            if failIf(attr):
                raise TypeError('private attribute change: ' + attr)
            else:
                return object.__setattr__(self, attr, value)

        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes
        return aClass
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))



#------------------------------------------------------------------------------

"""
@Private('age')
class Person:
    def __init__(self, name):
        self.age = 42               # <=== FAILS
        self.name = name
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
        self.age += yrs

X = Person('bob')
try:   X.age
except Exception as E: print(E)
print(X.name)
print(X)       # __str__
X + 10         # __add__
print(X)       # __str__


@Public('seq', '__getitem__', '__call__', '__getslice__')   # probably want Private here
class Person:                                               # or allow __X__ to pass always
    def __init__(self):
        self.seq = 'spam'
    def __getitem__(self, ix): return self.seq[ix]
    def __call__(self, *args): return ('call',) + args

X = Person()
try:   X.age
except Exception as E: print(E)
print(X.seq)
print(X[1:3])  # __getitem__
print(X(9))    # __call__
"""