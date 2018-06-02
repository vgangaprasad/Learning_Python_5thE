# File classscope.py

X = 1

def nester():
   print(X)                 # Global: 1
   class C:
       print(X)             # Global: 1
       def method1(self):
           print(X)         # Global: 1 
       def method2(self):
           X = 3            # Hides gobal
           print(X)         # Local: 3
   I = C()
   I.method1()
   I.method2()    

print(X)                    # Global: 1
nester()                    # Rest: 1, 1, 1, 3
print('-'*40)



X = 1

def nester():
   X = 2                    # Hides global
   print(X)                 # Local: 2
   class C:
       print(X)             # In enclosing def (nester): 2
       def method1(self):
           print(X)         # In enclosing def (nester): 2 
       def method2(self):
           X = 3            # Hides enclosing (nester)
           print(X)         # Local: 3
   I = C()
   I.method1()
   I.method2()    

print(X)                    # Global: 1
nester()                    # Rest: 2, 2, 2, 3
print('-'*40)



X = 1

def nester():
   X = 2                    # Hides global
   print(X)                 # Local: 2
   class C:
       X = 3                # Class local hides nester's: C.X or I.X (not scoped)
       print(X)             # Local: 3
       def method1(self):
           print(X)         # In enclosing def (not class!): 2 
           print(self.X)    # Inherited class local: 3
       def method2(self):
           X = 4            # Hides enclosing (nester, not class)
           print(X)         # Local: 4
           self.X = 5       # Hides class
           print(self.X)    # Located in instance: 5
   I = C()
   I.method1()
   I.method2()    

print(X)                    # Global: 1
nester()                    # Rest: 2, 3, 2, 3, 4, 5 
print('-'*40)
