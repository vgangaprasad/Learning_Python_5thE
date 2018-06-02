def countLines(name):
    file = open(name)
    return len(file.readlines())

def countChars(name):
    return len(open(name).read())

def test(name):                                  # Or pass file object
    return countLines(name), countChars(name)    # Or return a dictionary

if __name__ == '__main__':
    print(test('mymod.py'))
