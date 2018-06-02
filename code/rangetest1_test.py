# File rangetest1_test.py
from __future__ import print_function # 2.X
from rangetest1 import rangetest
print(__debug__)                           # False if "python -O main.py"

@rangetest((1, 0, 120))                    # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):                   # age must be in 0..120
    print('%s is %s years old' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

class Person:
    def __init__(self, name, job, pay):
        self.job  = job
        self.pay  = pay

    @rangetest([1, 0.0, 1.0])              # giveRaise = rangetest(...)(giveRaise)
    def giveRaise(self, percent):          # Arg 0 is the self instance here
        self.pay = int(self.pay * (1 + percent))

# Comment lines raise TypeError unless "python -O" used on shell command line

persinfo('Bob Smith', 45)                  # Really runs onCall(...) with state
#persinfo('Bob Smith', 200)                # Or person if -O cmd line argument

birthday(5, 31, 1963)
#birthday(5, 32, 1963)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)                         # Really runs onCall(self, .10)
print(sue.pay)                             # Or giveRaise(self, .10) if -O
#sue.giveRaise(1.10)
#print(sue.pay)
