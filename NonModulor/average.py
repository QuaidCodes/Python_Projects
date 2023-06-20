
# Returns the average of n numbers from the user

def average(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += int(numbers[i])

    return sum / len(numbers)


numbers = input("Enter a list of numbers without characters in between: ")
numbers = numbers.split(" ")

print(average(numbers))




