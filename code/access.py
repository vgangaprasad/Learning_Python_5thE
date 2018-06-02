"""
File access.py (3.X + 2.X)
Class decorator with Private and Public attribute declarations.
Controls external access to attributes stored on an instance, or 
inherited by it from its classes in any fashion.

Private declares attribute names that cannot be fetched or assigned 
outside the decorated class, and Public declares all the names that can.

Caveats: in 3.X catches built-ins coded in BuiltinMixins only (expand me);
as coded, Public may be less useful than Private for operator overloading.
"""
from access_builtins import BuiltinsMixin    # A partial set!

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)

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
