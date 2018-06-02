class Animal:
    def reply(self):   self.speak()              # Back to subclass
    def speak(self):   print('spam')             # Custom message

class Mammal(Animal):
    def speak(self):   print('huh?')

class Cat(Mammal):
    def speak(self):   print('meow')

class Dog(Mammal):
    def speak(self):   print('bark')

class Primate(Mammal):
    def speak(self):   print('Hello world!')

class Hacker(Primate): pass                      # Inherit from Primate
