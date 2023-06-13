#

class Author:
    # Class Variables (Default variable in the class, can be called without instantiating a class)
    name = 'Quaid Tahir'
    gender = 'Male'
    age = 23
    email = "QuaidTahir@quaidtahir.com"

    # Constructor
    def __init__(self, name, gender, age, email):  # Variables created upon an instance
        self.name = name  # Instance Variable
        self.gender = gender  # Instance Variable
        self.age = age  # Instance Variable
        self.email = email  # Instance Variable

    # Destructor
    def __del__(self):  # Python has a garbage collector that handles memory management automatically, unlike C+,
        ...             # therefore no need for a destructor.

    def name_setter(self, name):
        self.name = name

    def gender_setter(self, gender):
        self.gender = gender

    def age_setter(self, age):
        self.age = age

    def email_setter(self, email):
        self.email = email

    def name_getter(self):
        return self.name

    def gender_getter(self):
        return self.gender

    def age_getter(self):
        return self.age

    def email_getter(self):
        return self.email

    @staticmethod  # Static methods can be called without instantiating an object.
    def this_static_method():
        print("Hello, I am static")


author = Author('Quaid Butt', 'M', 24, 'quaidtahir@quaidtahir.net')

# print(author.name_getter())
# print(author.age_getter())
# print(author.gender_getter())
# print(author.email_getter())

del author  # Deletes the instance


class Father:
    def __init__(self):
        self.name = 'father'
        self.age = 41


class Child(Father()):
    def __init__(self):
        self.name = 'son ' + Father().name + ' ' + str(Father().age)

    def get_name(self):
        return self.name


child_obj = Child()

print(child_obj.get_name())

del child_obj
