#!python
# File testmixin.py (2.X + 3.X)
"""
Generic lister mixin tester: similar to transitive reloader in 
Chapter 25, but passes a class object to tester (not function),
and testByNames adds loading of both module and class by name 
strings here, in keeping with Chapter 31's factories pattern.
"""
import importlib

def tester(listerclass, sept=False):

    class Super:
        def __init__(self):            # Superclass __init__
            self.data1 = 'spam'        # Create instance attrs
        def ham(self):
            pass

    class Sub(Super, listerclass):     # Mix in ham and a __str__
        def __init__(self):            # Listers have access to self
            Super.__init__(self)
            self.data2 = 'eggs'        # More instance attrs
            self.data3 = 42
        def spam(self):                # Define another method here
            pass

    instance = Sub()                   # Return instance with lister's __str__
    print(instance)                    # Run mixed-in __str__ (or via str(x))
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject   = importlib.import_module(modname)  # Import by namestring
    listerclass = getattr(modobject, classname)     # Fetch attr by namestring
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance',  'ListInstance',  True)      # Test all 3 here
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree',      'ListTree',      False)
