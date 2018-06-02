"""
Catch built-ins: inline redefinition option
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            def __str__(self):
                return str(self.__wrapped)
            def __add__(self, other):
                return self.__wrapped + other         # Or getattr(x, '__add__')(y)
            def __getitem__(self, index):
                return self.__wrapped[index]          # If needed
            def __call__(self, *args, **kargs):
                return self.__wrapped(*args, **kargs) # If needed
            # plus any others needed

            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


#------------------------------------------------------------------------------


@Private('age')
class Person:
    def __init__(self, name):
        self.age = 42
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
c:\code>py -3 access2_builtins1.py
private attribute fetch: age
bob
Person: 42
Person: 52
private attribute fetch: age
spam
pa
('call', 9)
"""

