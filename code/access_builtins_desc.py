"""
File access_builtins_desc.py (from access_builtins.py)
Route some built-in operations back to proxy class __getattr__, so they
work same in 3.X as direct by-name calls and 2.X's default classic classes.
Expand me as needed to include other __X__ names used by proxied objects.

This version auto creates class-level descriptors to intercept builtins, 
and assumes a _wrapped in the instaces referencing the proxied object.
It responds to attribute access, not the actual built-in oeration call.
"""

"""
original...

class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):                                             
        return self.reroute('__add__', other)         
    def __str__(self):
        return self.reroute('__str__')        
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)

    # Plus any others used by wrapped objects in 3.X only
"""



class BuiltinsMixin:
    class ProxyDesc(object):                                     # object for 2.X
        def __init__(self, attrname):
            self.attrname = attrname
        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)     # Assume a _wrapped
        
    builtins = ['add', 'str', 'getitem', 'call']                 # Plus others
    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))   


  # The loop does:
  # __add__ = ProxyDesc("__add__")
  # __str__ = ProxyDesc("__str__")
  # ...