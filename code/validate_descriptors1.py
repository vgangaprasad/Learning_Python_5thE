# File validate_descriptors1.py: using shared descriptor state

class CardHolder(object):                        # Need all "(object)" in 2.X only
    acctlen = 8                                  # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __set__ calls too!
        self.age  = age                          # __X not needed: in descriptor
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    class Name(object):
        def __get__(self, instance, owner):      # Class names: CardHolder locals
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()

    class Age(object):                                  
        def __get__(self, instance, owner):
            return self.age                             # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct(object):                                 
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:          # Use instance class data
                raise TypeError('invald acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain(object):                              
        def __get__(self, instance, owner):
            return instance.retireage - instance.age    # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')        # Else set allowed here
    remain = Remain()
