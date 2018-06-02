from __future__ import print_function

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

print('making class')
class Spam:                               # Inherits from none, instance of MetaOne
    __metaclass__ = MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
print(Spam.__bases__, X.__getattribute__, Spam.__mro__)