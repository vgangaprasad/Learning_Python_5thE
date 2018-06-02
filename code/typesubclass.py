# Subclass built-in list type/class
# Map 1..N to 0..N-1; call back to built-in version.

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')               # __init__ inherited from list
    print(x)                        # __repr__ inherited from list

    print(x[1])                     # MyList.__getitem__
    print(x[3])                     # Customizes list superclass method

    x.append('spam'); print(x)      # Attributes from list superclass
    x.reverse();      print(x)
