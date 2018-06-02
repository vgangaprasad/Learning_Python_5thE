"""
File timerdeco-test.py
"""
from __future__ import print_function # 2.X
from timerdeco import timer
import sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

print('---------------------------------------------------')
# Test on functions

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]         # listcomp(...) triggers onCall

@timer('[MMM]==>')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))   # list() for 3.X views

for func in (listcomp, mapcall):
    result = func(5)                  # Time for this call, all calls, return value
    func(5000000)
    print(result)
    print('allTime = %s\n' % func.alltime)   # Total time for all calls

print('---------------------------------------------------')
# Test on methods

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @timer()
    def giveRaise(self, percent):            # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)          # tracer remembers giveRaise

    @timer(label='**')
    def lastName(self):                      # lastName = timer(...)(lastName)
        return self.name.split()[-1]         # alltime per class, not instance

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)                           # runs onCall(sue, .10)
print(int(bob.pay), int(sue.pay))
print(bob.lastName(), sue.lastName())        # runs onCall(bob), remembers lastName
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))

