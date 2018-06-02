X = 11                        # My X: global to this file only

import moda                   # Gain access to names in moda
moda.f()                      # Sets moda.X, not this file's X
print(X, moda.X)
