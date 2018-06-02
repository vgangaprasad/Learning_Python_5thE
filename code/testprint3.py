from print3_alt2 import print3
print3(1, 2, 3)
print3(1, 2, 3, sep='')                     # Suppress separator
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')             # Various object types

print3(4, 5, 6, sep='', end='')             # Suppress newline
print3(7, 8, 9)
print3()                                    # Add newline (or blank line)

import sys
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)    # Redirect to file
