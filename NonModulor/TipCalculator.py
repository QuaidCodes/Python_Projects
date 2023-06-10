
# Tip calculator

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? "))/100
numOfPeople = int(input("How many people to split the bill? "))

if numOfPeople <= 0 or bill < 1:
    print("Excuse me, Who ate the food?")
elif numOfPeople == 1:
    tip = bill * percentage
    print(f"You should tip {tip}")
else:
    tip = (bill / numOfPeople) * percentage
    bill = bill/numOfPeople
    totalBill = round(tip + bill, 2)

    print(f"Each person should pay ${totalBill}, in which ${round(tip, 2)} is tip and ${round(bill, 2)} is the food bill.")