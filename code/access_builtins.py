"""
File access_builtins.py (from access2_builtins2b.py)
Route some built-in operations back to proxy class __getattr__, so they
work same in 3.X as direct by-name calls and 2.X's default classic classes.
Expand me as needed to include other __X__ names used by proxied objects.
"""

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
