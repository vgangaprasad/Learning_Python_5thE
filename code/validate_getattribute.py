# File validate_getattribute.py

class CardHolder(object):                        # Need "(object)" in 2.X only
    acctlen = 8                                  # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattribute__(self, name):
        superget = object.__getattribute__             # Don't loop: one level up
        if name == 'acct':                             # On all attr fetches
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)                # name, age, addr: stored

    def __setattr__(self, name, value):
        if name == 'name':                             # On all attr assignments
            value = value.lower().replace(' ', '_')    # addr stored directly
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                     # Avoid loops, orig names
