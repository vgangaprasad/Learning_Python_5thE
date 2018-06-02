class PrivateExc(Exception): pass                   # More on exceptions in Part VII

class Privacy:
    def __setattr__(self, attrname, value):         # On self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)        # Make, raise user-define except
        else:
            self.__dict__[attrname] = value         # Avoid loops by using dict key

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'               # To do better, see Chapter 39!

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'      # Works
   #y.name = 'Sue'      # Fails
    print(x.name)

    y.age  = 30         # Works
   #x.age  = 40         # Fails
    print(y.age)

