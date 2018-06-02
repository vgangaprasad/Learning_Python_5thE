# Code here was run interactively
# tests in Chapter 31's lister example

from mapattr import *
from testmixin0 import Sub
I = Sub()
#trace(I.__dict__.keys())        # in instance

trace(dflr(I.__class__))        # 2.X search order
trace(inheritance(I))           # inheritance class order

trace(mapattrs(I))

trace(mapattrs(I, bysource=True))

trace(mapattrs(I, withobject=True))

amap = mapattrs(I, withobject=True, bysource=True)
trace(amap)

