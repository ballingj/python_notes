"""
OOP - an approach to programming that involves modeling 'things' into python obkects.
These objects can contain both data and functions all wrapped together into a reuseable component.

class: is how we create objects for OOP.  This is the recipe or template that we use to create objects.
"""

#define a class called Dog
from io import BufferedReader


class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []        # list of tricks
    """ method to bark"""
    def bark(self):
        print(f"{self.name} says WOOF!")

    """method to add trick to the list of tricks"""
    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
    """method to perform a trick - check first"""
    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick}")

#instantiate a Dog instance
elton = Dog("Elton", "Aussie", "Omaha")
print(elton.name, elton.breed, elton.location)   # Elton Aussie Omaha
print(elton.tricks) # []

#instantiate another Dog
venice = Dog("Venice", "Border Collie", "Bellevue")
print(venice.name, venice.breed, venice.location)   # Venice Shepherd Bellevue
print(venice.tricks)  # []
venice.bark()


# adding methods to a Class
"""
# add this function to the Dog class
def add_trick(self, new_trick):
    self.tricks.append(new_trick)
"""
elton.learn_trick("sit")
print(elton.name, elton.tricks)
elton.perform_trick("sit")


# Class Attributes
################################
"""
Class Attributes: are variables and methods that will be common to all instances.  
They are defined in the class definition.
"""
class Cat:
    species = "feline"  # value will be common to all Cat instance

    #@classmethod is a decorator
    # this method will be function to be executed on a class Cat: not the instance of a Cat
    @classmethod   
    def register_stray(cls):
        return cls("coming soon", "unknown", "unknown")   # corresponds to unknow values of name, breed, location

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
    def meow(self):
        print(self.name, "meows")

stray1 = Cat.register_stray()
stray2 = Cat.register_stray()
print("Strays: ", stray1.name, stray1.breed, stray1.location)
stray1.meow()
douglas = Cat("Douglas", "yellow tabby", "Papillion")
print(douglas.name, douglas.breed, douglas.location)
douglas.meow()

# Class Inheritance
################################
"""class inheritance: allows for an existing class to be copied to another class, so as to inherit the properties and methods already defined in that class being copied"""
class Lion(Cat):
    def roar(self):
        print(self.name, "ROAARRRR!")

eli = Lion("Eli", "African Lion", "Henry Doorley Zoo")
eli.meow()      # from the Cat method
eli.roar()      # from the Lion method
print(eli.name, eli.breed, eli.location)  # Eli African Lion Henry Doorley Zoo

# super() function
########################################
"""
use the super() method to refer to the base/parent's properties
this is required when the subclass has to have an __init__ method that overwrites the inherited
properties in the case of having additional properies not already in the parent/base class
"""

class Cougar(Cat):
    def __init__(self, name, breed, location, pride_name):
        super().__init__(name, breed, location)
        self.pride_name = pride_name    # this is the additional property only in Cougar class
    def purr(self):
        print(self.name, "Puuuurrrrrs")

marissa = Cougar("marissa_tomei", "human", "Hollywood", "Hot Cougar" )
print(marissa.name, marissa.breed, marissa.location, marissa.pride_name)
marissa.purr()
