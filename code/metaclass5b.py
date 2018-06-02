class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):      # By name, not built-in
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(SuperMeta):                                  # Created by type default
    def __init__(Class, classname, supers, classdict):     # Overrides type.__init__
        print('In SubMeta init:', classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                   # Not a data descriptor if found by name
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})  # Explicit calls work: class inheritance
print()
SubMeta('yyy', (), {})                    # But implicit built-in calls do not: type
