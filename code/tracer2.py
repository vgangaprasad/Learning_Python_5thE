def tracer(func):                      # Remember original
    def oncall(*args):                 # On later calls
        oncall.calls += 1           
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self,a, b, c): return a + b + c

x = C()
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))           # Same output as tracer1 (in tracer2.py)
