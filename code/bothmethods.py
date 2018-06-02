# File bothmethods.py

class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    def smeth(x):                  # Static: no instance passed
        print([x])

    def cmeth(cls, x):             # Class: gets class, not instance
        print([cls, x])

    smeth = staticmethod(smeth)    # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth)     # Make cmeth a class method (or @: ahead)
