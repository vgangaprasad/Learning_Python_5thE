from setwrapper import Set

class MultiSet(Set):
    """
    Inherits all Set names, but extends intersect and union to support
    multiple operands; note that "self" is still the first argument 
    (stored in the *args argument now); also note that the inherited 
    & and | operators call the new methods here with 2 arguments, but 
    processing more than 2 requires a method call, not an expression;
    intersect doesn't remove duplicates here: the Set constructor does;
    """
    def intersect(self, *others):
        res = []
        for x in self:                         # Scan first sequence
            for other in others:               # For all other args
                if x not in other: break       # Item in each one?
            else:                              # No: break out of loop
                res.append(x)                  # Yes: add item to end
        return Set(res)

    def union(*args):                          # self is args[0]
        res = []
        for seq in args:                       # For all args
            for x in seq:                      # For all nodes
                if not x in res:
                    res.append(x)              # Add new items to result
        return Set(res)
