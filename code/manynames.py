X = 11                       # Global (module) name/attribute (X, or manynames.X)

def f():
    print(X)                 # Access global X (11)

def g():
    X = 22                   # Local (function) variable (X, hides module X)
    print(X)

class C:
    X = 33                   # Class attribute (C.X)
    def m(self):
        X = 44               # Local variable in method (X)
        self.X = 55          # Instance attribute (instance.X)

if __name__ == '__main__':
    print(X)                 # 11: module (a.k.a. manynames.X outside file)
    f()                      # 11: global
    g()                      # 22: local
    print(X)                 # 11: module name unchanged

    obj = C()                # Make instance
    print(obj.X)             # 33: class name inherited by instance

    obj.m()                  # Attach attribute name X to instance now
    print(obj.X)             # 55: instance
    print(C.X)               # 33: class (a.k.a. obj.X if no X in instance)

    #print(C.m.X)            # FAILS: only visible in method
    #print(g.X)              # FAILS: only visible in function
