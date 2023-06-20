# Prevents a user from creating an object of that class.
# compels user to override abstract methods in a child class.

# Abstract Classes - a class that contains one or more abstract methods.
# Abstract method - a method that has a declaration but does not have an implementation.

# Any children of the an abstract class as a parent will be required to

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        ...

    @abstractmethod
     def stop(self):
        ...
class Car(Vehicle):

    def go(self):
        print("You drive the car.")

    def stop(self):
        print("This car is stopped.")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive this motorcycle.")

    def stop(self):
        print("This car is stopped.")

#vehicle = Vehicle() # Cannot create an instance of an abstract class
car = Car()
motorcycle = Motorcycle()

# vehicle.go() # Cannot call a method from an abstract class
car.go()
motorcycle.go()



