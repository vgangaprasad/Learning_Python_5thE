from nested1 import X, printer    # Copy names out
X = 88                            # Changes my "X" only!
printer()                         # nested1's X is still 99
