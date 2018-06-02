"""
pybench2_cases.py: Run pybench2 on a set of pythons and statements.

Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just 
one specific version on stmts, "pybench_cases.py -a" to test all pythons 
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import pybench2, sys

pythons = [                                                     # (ispy3?, path)
    (1, 'C:\python33\python'),
    (0, 'C:\python27\python'),
    (0, 'C:\pypy\pypy-1.9\pypy')
]

stmts = [                                                       # (num,rpt,setup,stmt)
    (0, 0, "", "[x ** 2 for x in range(1000)]"),                                                
    (0, 0, "", "res=[]\nfor x in range(1000): res.append(x ** 2)"),     # \n=multistmt
    (0, 0, "", "$listif3(map(lambda x: x ** 2, range(1000)))"),         # \n\t=indent
    (0, 0, "", "list(x ** 2 for x in range(1000))"),                    # $=list or ''

#   (0, 0, "", "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),  
#   (0, 0, "", "s = '?'\nfor i in range(10000): s += '?'"),

    (0, 0, "def f(x):\n\treturn x", 
           "[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x):\n\treturn x", 
           "res=[]\nfor x in 'spam' * 2500:\n\tres.append(f(x))"),

    (0, 0, "L = [1, 2, 3, 4, 5]", "for i in range(len(L)): L[i] += 1"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "i=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"),
]

tracecmd = '-t' in sys.argv                           # -t: trace commmand lines?
pythons  = pythons if '-a' in sys.argv else None      # -a: all in list, else one?
pybench2.runner(stmts, pythons, tracecmd)
