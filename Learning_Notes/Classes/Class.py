
# Basic Classes
# -----------------------------------------
class Car:

    # class variable - declared within a class but outside the scope of a constructor
    seats = 5

    # Constructor
    def __init__(self, name, make, speed):
        # instance variables - declared inside a constructor and can be assigned a unique value
        self.name = name
        self.make = make
        self.speed = speed

    # Destructor
    def __del__(self):
        ...

# -----------------------------------------
