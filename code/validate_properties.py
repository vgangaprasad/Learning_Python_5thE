# File validate_properties.py

class CardHolder(object):                      # Need "(object)" for setter in 2.X
    acctlen = 8                                # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                       # Instance data
        self.name = name                       # These trigger prop setters too!
        self.age  = age                        # __X mangled to have class name
        self.addr = addr                       # addr is not managed
                                               # remain has no data
    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):                       # Could be a method, not attr
        return self.retireage - self.age       # Unless already using as attr
    remain = property(remainGet)
