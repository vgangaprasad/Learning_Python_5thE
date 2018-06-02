X = 88                        # My X: global to this file only
def f():
    global X                  # Change this file's X
    X = 99                    # Cannot see names in other modules
