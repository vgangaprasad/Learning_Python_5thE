"""
reloadall2.py: transitively reload nested modules (alternative coding)
"""

import types
from imp import reload                              # from required in 3.X
from reloadall import status, tryreload, tester

def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) == types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)                          # Reload this, recur to attrs
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)

def reload_all(*args): 
    transitive_reload(args, set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall2')                # Test code: reload myself?
