
# Derived and Base Classes
# -----------------------------------------
# Base Class
class Animal:
    honey = "Bears eats honey"

    def eat(self):
        return True

    def sleeping(self):
        return True


# Derived Class
class Bears(Animal):
    def __init__(self):
        self.honey = Animal.honey

    def Honey(self):
        Animal.eat(self)
# -----------------------------------------

# Class Instantiation
obj1 = Bears()

print(obj1.honey)
