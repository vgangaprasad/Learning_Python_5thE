def sumtree(L):
    tot = 0
    for x in L:                                  # For each item at this level
        if not isinstance(x, list):
            tot += x                             # Add numbers directly
        else:
            tot += sumtree(x)                    # Recur for sublists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
