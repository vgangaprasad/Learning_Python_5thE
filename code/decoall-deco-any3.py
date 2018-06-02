# Class decorator factory: apply any decorator to all methods of a class

from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))        # Not __dict__
        return aClass
    return DecoDecorate

#@decorateAll(tracer)                          # Use a class decorator
#@decorateAll(tracer(timer(label='@@')))  

#@decorateAll(timer(label='@@')(tracer))      # Times applying the tracer!
#@decorateAll(tracer(timer(label='@@')))      # Traces applying the timer!

#@decorateAll(tracer)                          # Traces onCall wrapper, times methods
#@decorateAll(timer(label='@@'))

#@decorateAll(timer(label='@@'))
#@decorateAll(tracer)                          # Times onCall wrapper, traces methods

   
@decorateAll(timer(label='@@'))
@decorateAll(tracer)                       # Times onCall wrapper, traces methods
class Person:                                 # Applies func decorator to methods
    def __init__(self, name, pay):            # Person = decorateAll(..)(Person)
        self.name = name                      # Person = DecoDecorate(Person)
        self.pay  = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())

# If using timer: total time per method
"""
print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)
"""