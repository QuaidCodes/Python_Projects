
# Leap year finder

currYear = int(input("Enter any year to check if it is a leap year: "))

if currYear % 4 == 0:
    if currYear % 100 == 0:
        if currYear % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")