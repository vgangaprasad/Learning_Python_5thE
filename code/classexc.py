class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()          # Raise superclass instance
    raise X

def raiser1():
    X = Specific1()        # Raise subclass instance
    raise X

def raiser2():
    X = Specific2()        # Raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:        # Match General or any subclass of it
        import sys
        print('caught: %s' % sys.exc_info()[0])
