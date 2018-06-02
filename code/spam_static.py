class Spam:
    numInstances = 0                         # Use static method for class data
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances():                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)
