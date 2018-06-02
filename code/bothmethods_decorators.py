# File bothmethods_decorators.py

class Methods(object):             # object needed in 2.X for property setters
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def smeth(x):                  # Static: no instance passed
        print([x])

    @classmethod
    def cmeth(cls, x):             # Class: gets class, not instance
        print([cls, x])

    @property                      # Property: computed on fetch
    def name(self):
        return 'Bob ' + self.__class__.__name__
