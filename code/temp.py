from __future__ import print_function

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

print('making class')
class Spam:                               # Inherits from Eggs, instance of Meta
    __metaclass__ = MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        pass

print('making instance')
X = Spam()
print('data: ', X.data)
