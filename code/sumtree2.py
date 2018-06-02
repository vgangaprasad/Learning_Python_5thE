trace = lambda x: None               # or print
visit = lambda x: print(x, end=', ')


# breadth-first by items: add to end

def sumtree(L):                                  # Breadth-first, explicit queue
    tot = 0
    items = list(L)                              # Start with copy of top level
    while items:
        trace(items)
        front = items.pop(0)                     # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                         # Add numbers directly
            visit(front)
        else:
            items.extend(front)                  # <== Append all in nested list
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
print('-'*40)



# depth-first by items: add to front (like recursive calls version)

def sumtree(L):                                  # Depth-first, explicit stack
    tot = 0
    items = list(L)                              # Start with copy of top level
    while items:
        trace(items)
        front = items.pop(0)                     # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                         # Add numbers directly
            visit(front)
        else:
            items[:0] = front                    # <== Prepend all in nested list
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
print('-'*40)



# Breadth-first by levels

def sumtree(L):
    tot = 0
    levels = [L]
    while levels:
        trace(levels)
        front = levels.pop(0)                    # Fetch/delete front path
        for x in front:
            if not isinstance(x, list):
                tot += x                         # Add numbers directly
                visit(x)
            else:
                levels.append(x)                 # Push/schedule nested lists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
print('-'*40)


