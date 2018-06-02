"""
reloadall3.py: transitively reload nested modules (explicit stack)
"""

import types
from imp import reload                              # from required in 3.X
from reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()                        # Delete next item at end
        status(next)                                # Reload this, push attrs
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3')                # Test code: reload myself?
