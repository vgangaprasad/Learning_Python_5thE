def countLines(file):
    file.seek(0)                                 # Rewind to start of file
    return len(file.readlines())

def countChars(file):
    file.seek(0)                                 # Ditto (rewind if needed)
    return len(file.read())

def test(name):
    file = open(name)                            # Pass file object
    return countLines(file), countChars(file)    # Open file only once
