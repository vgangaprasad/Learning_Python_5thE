"""
File argtest.py: (3.X + 2.X) function decorator that performs 
arbitrary passed-in validations for arguments passed to any 
function method. Range and type tests are two example uses;
valuetest handles more arbitrary tests on a argument's value.

Arguments are specified by keyword to the decorator. In the actual 
call, arguments may be passed by position or keyword, and defaults
may be omitted.  See self-test code below for example use cases.

Caveats: doesn't fully support nesting because call proxy args 
differ; doesn't validate extra args passed to a decoratee's *args;
and may be no easier than an assert except for canned use cases.
"""
trace = False


def rangetest(**argchecks): 
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])

def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))

def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))


def argtest(argchecks, failif):             # Validate args per failif + criteria
    def onDecorator(func):                  # onCall retains func, argchecks, failif
        if not __debug__:                   # No-op if "python -O main.py args..."
            return func                     
        else:
            code = func.__code__
            expected = list(code.co_varnames[:code.co_argcount])
            def onError(argname, criteria):
                 errfmt = '%s argument "%s" not %s'
                 raise TypeError(errfmt % (func.__name__, argname, criteria))

            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():      # For all to test
                    if argname in kargs:                           # Passed by name
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)

                    elif argname in positionals:                   # Passed by posit
                        position = positionals.index(argname)
                        if failif(pargs[position], criteria):
                            onError(argname, criteria)
                    else:                                          # Not passed-dflt
                        if trace:
                            print('Argument "%s" defaulted' % argname)
                return func(*pargs, **kargs)   # OK: run original call
            return onCall
    return onDecorator


if __name__ == '__main__':
    import sys
    def fails(test):
        try:    result = test()
        except: print('[%s]' % sys.exc_info()[1])
        else:   print('?%s?' % result)

    print('--------------------------------------------------------------------')
    # Canned use cases: ranges, types

    @rangetest(m=(1, 12), d=(1, 31), y=(1900, 2013))
    def date(m, d, y):
        print('date = %s/%s/%s' % (m, d, y))

    date(1, 2, 1960)
    fails(lambda: date(1, 2, 3))

    @typetest(a=int, c=float)
    def sum(a, b, c, d): 
        print(a + b + c + d)

    sum(1, 2, 3.0, 4) 
    sum(1, d=4, b=2, c=3.0)               
    fails(lambda: sum('spam', 2, 99, 4)) 
    fails(lambda: sum(1, d=4, b=2, c=99)) 

    print('--------------------------------------------------------------------')
    # Arbitrary/mixed tests

    @valuetest(word1=str.islower, word2=(lambda x: x[0].isupper()))
    def msg(word1='mighty', word2='Larch', label='The'):
        print('%s %s %s' % (label, word1, word2))

    msg()  # word1 and word2 defaulted
    msg('majestic', 'Moose')
    fails(lambda: msg('Giant', 'Redwood'))
    fails(lambda: msg('great', word2='elm'))

    print('--------------------------------------------------------------------')
    # Manual type and range tests

    @valuetest(A=lambda x: isinstance(x, int), B=lambda x: x > 0 and x < 10)    
    def manual(A, B): 
        print(A + B)

    manual(100, 2)
    fails(lambda: manual(1.99, 2))
    fails(lambda: manual(100, 20))

    print('--------------------------------------------------------------------')
    # Nesting: runs both, by nesting proxies on original.
    # Open issue: outer levels do not validate positionals due 
    # to call proxy function's differing argument signature;
    # when trace=True, in all but the last of these "X" is 
    # classified as defaulted due to the proxy's signature.

    @rangetest(X=(1, 10)) 
    @typetest(Z=str)                      # Only innermost validates positional args
    def nester(X, Y, Z): 
        return('%s-%s-%s' % (X, Y, Z))

    print(nester(1, 2, 'spam'))                # Original function runs properly
    fails(lambda: nester(1, 2, 3))             # Nested typetest is run:  positional
    fails(lambda: nester(1, 2, Z=3))           # Nested typetest is run:  keyword
    fails(lambda: nester(0, 2, 'spam'))        # <==Outer rangetest not run: posit.
    fails(lambda: nester(X=0, Y=2, Z='spam'))  # Outer rangetest is run:  keyword
