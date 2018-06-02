class Wrapper(object):
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)              # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch
