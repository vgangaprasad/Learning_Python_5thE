# Try to Import module in same directory as me, but:

#from . import m1  # <==OK in package, not allowed in non-package mode in 2.X + 3.X
#import m1         # <==OK in program, fails to check package's own dir in 3.X

# set PYTHONPATH=c:\code
import dualpkg.m1 as m1     # <==works in both modes if sys.path includes pks root
 
def somefunc():
    m1.somefunc()
    print('m2.somefunc')

if __name__ == '__main__':
   somefunc()               # Self-test or top-level script code