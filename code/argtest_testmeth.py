from argtest import rangetest, typetest

class C:
    @rangetest(a=(1, 10))
    def meth1(self, a): 
        return a * 1000

    @typetest(a=int)
    def meth2(self, a): 
        return a * 1000 

"""
>>> from argtest_testmeth import C
>>> X = C()
>>> X.meth1(5)
5000
>>> X.meth1(20)
TypeError: meth1 argument "a" not (1, 10)
>>> X.meth2(20)
20000
>>> X.meth2(20.9)
TypeError: meth2 argument "a" not <class 'int'>
""" 