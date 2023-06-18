# Method Overriding
# Method signature is a combination of a methods name and its parameter
# An object will use its own methods before searching the parent class methods and attr. like specification in CSS
class Animal:

    def eat(self):
        print("This animal is eating.")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot.")

rabbit = Rabbit()
rabbit.eat()
