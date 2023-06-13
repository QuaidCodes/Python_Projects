
# Name: Love Calculator
# Description:  Provides the compatibility between partners, by using superstitious logic.
print("Welcome to love calculator!")

name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

name = (name1 + name2).lower()

true = "true"
love = "love"

count = 0
count2 = 0
for i in range(len(true)):
    count += name.count(true[i])
    count2 += name.count(love[i])

score = int(str(count) + str(count2))

if score == 100 or score > 100:
    if score == 100:
        print(f"Your score is {score}, you are like Anakin and Padme.")
    else:
        print("Your score is 100, you are like Anakin and Padme.")
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")