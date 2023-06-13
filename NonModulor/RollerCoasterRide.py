
# RollerCoaster ride

print("Welcome to Dark Vader Park's infamous RollerCoaster ride.")

height = float(input("What is your height in cm? "))
bill = 0

adultTicket = 15
youthTicket = 12
minorTicket = 0
photoCharge = 5

if height >= 152.4:
    age = int(input("How old are you? "))

    if age >= 18:
        bill = adultTicket
    elif age > 10:
        bill = youthTicket
    else:
        bill = minorTicket
        print("You can ride for free, because Darth Vader adores kids.")

    response = input("Would you like to take pictures on the ride for $5 dollars? y/Y or n/N: ")

    if response == 'y' or response == 'Y':
        if age >= 18:
            bill += photoCharge
        elif age > 10:
            bill += photoCharge
        else:
            bill += minorTicket

    print(f"Your total bill is {bill}, enjoy! Regards, Darth Vader.")
else:
    print("You are too short, drink more milk, eat more meat, and exercise everyday to grow taller.")