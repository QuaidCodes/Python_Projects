# Multi-level inheritance


# Parent Class
class Organism:
    alive = True

# 1st Child Class, inherits from Organism parent class
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

# 2nd Child Class, inherits from Animal 1st child class
class Cat(Animal):
    def yawn(self):
        print("This Cat is yawning.")

# cat instances wil have access to all the methods and attributes from Organism and Animal Class.
cat = Cat()

print(Cat.alive)  # Organism Class attribute access via Cat class instance
cat.eat()         # Animal Class method accessed by Cat class instance
cat.yawn()        # Cat class method
