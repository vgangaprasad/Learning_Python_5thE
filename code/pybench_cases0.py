"""
(temporary work copy)

pybench_cases2.py: This is an extension with additional
stmts and pythons: uncomment/change items here to test.
"""

import pybench, sys

pythons = [                                        # format=(ispy3?, exepath)
    (0, 'C:\python27\python'),
    (1, 'C:\python32\python'),
    (1, 'C:\python33\python'),
    (0, 'C:\pypy\pypy-1.9\pypy'),
    (0, 'C:\pypy\pypy-2.0-beta1\pypy')
]

stmts = [                                          # format=(number?, repeat?, stmt)
# sequence ops ($listif3 => list or '')
#    (0, 0, "[x ** 2 for x in range(1000)]"),
#    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),     # \n\t=indent
#    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),         # \n=multiline
#    (0, 0, "list(x ** 2 for x in range(1000))"),                    # $=list or ''

# use function calls: map wins
#    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
#    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
#    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
#    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),

# user-defined function calls: same effect
    (0, 0, "def f(x): return x\n[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x): return x\nres=[]\nfor x in 'spam' * 2500: res.append(f(x))"),
    (0, 0, "def f(x): return x\n$listif3(map(f, 'spam' * 2500))"),
    (0, 0, "def f(x): return x\nlist(f(x) for x in 'spam' * 2500)"),

# set and dicts
#    (0, 0, "{x ** 2 for x in range(1000)}"),
#    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
#    (0, 0, "{x: x ** 2 for x in range(1000)}"),
#    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),

# more string tests
#    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
#    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),

# Iterations: for -a \t replaced with 4*' ', may fail some shells?
#    (0, 0, "L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1"),
#    (0, 0, "L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"),
#    (0, 0, "L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]"),

# Files: close() else may fail in pypy due to number of open files
#    (0, 0, "f=open('C:/Python33/Lib/pdb.py')\nfor line in f: x=line\nf.close()"),
#    (0, 0, "f=open('C:/Python33/Lib/pdb.py')\nfor line in f.readlines(): x=line\nf.close()"),
#    (0, 0, "f = open('C:/Python33/Lib/pdb.py')\n"
#           "while True:\n\tline = f.readline()\n\tif not line: break\n\tx = line\nf.close()")

# pathological: 300k digits
    (1, 1, "len(str(2**1000000))")  # pypy loses on this today
]

tracecmd = '-t' in sys.argv                           # -t: trace commmand lines?
pythons  = pythons if '-a' in sys.argv else None      # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)
