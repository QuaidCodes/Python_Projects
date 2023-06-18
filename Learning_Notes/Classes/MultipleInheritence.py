# Multiple inheritance

# Parent Class
class Prey:
    def flee(self):
        print("I flee!")


class Predator:
    def hunt(self):
        print("I hunt!")


class Wolf(Predator):  # Inherits Predator Class
    ...


class Rabbit(Prey):  # Inherits Prey Class
    ...


class Hawk(Predator):  # Inherits Predator Class
    ...


class Fish(Predator, Prey):  # Inherits both Prey and Predator class
    ...


# Instantiation
wolf = Wolf()
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()  # This instance inherits both Predator and Prey class

print("wolf: ", end=" ")
wolf.hunt()

print("rabbit: ", end=" ")
rabbit.flee()

print("hawk: ", end=" ")
hawk.hunt()

print("fish: ", end=" ")
fish.hunt()  # Predator class attribute
fish.flee()  # Prey class attribute
