# File validate_descriptors2.py: using per-client-instance state

class CardHolder(object):                        # Need all "(object)" in 2.X only
    acctlen = 8                                  # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Client instance data
        self.name = name                         # These trigger __set__ calls too!
        self.age  = age                          # __X needed: in client instance
        self.addr = addr                         # addr is not managed
                                                 # remain managed but has no data
    class Name(object):
        def __get__(self, instance, owner):      # Class names: CardHolder locals
            return instance.__name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value
    name = Name()                                       # class.name vs mangled attr

    class Age(object):
        def __get__(self, instance, owner):
            return instance.__age                       # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance.__age = value
    age = Age()                                         # class.age vs mangled attr

    class Acct(object):
        def __get__(self, instance, owner):
            return instance.__acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:          # Use instance class data
                raise TypeError('invald acct number')
            else:
                instance.__acct = value
    acct = Acct()                                       # class.acct vs mangled name

    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age    # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')        # Else set allowed here
    remain = Remain()
