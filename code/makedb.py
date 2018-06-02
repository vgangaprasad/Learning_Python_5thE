# File makedb.py: store Person objects on a shelve database

from person import Person, Manager               # Load our classes
bob = Person('Bob Smith')                        # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')                     # Filename where objects are stored
for object in (bob, sue, tom):                   # Use object's name attr as key
    db[object.name] = object                     # Store object on shelve by key
db.close()                                       # Close after making changes
