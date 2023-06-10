
# *args beginner
# pass in multiple arguments as a tuple

def multi(*args):
    total = 1

    for i in args:
        total *= i

    return total

print(multi(2,2,2,2,2))