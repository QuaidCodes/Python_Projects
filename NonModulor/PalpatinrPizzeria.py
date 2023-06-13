
# Palpatine Pizzeria

smallPizza = 12
mediumPizza = 17
largePizza = 20
bill = 0
totalBill = 0

def toppings(bill):
    toppingsList = ["Mayonese", "Pineapple", "Tatooine Cream", "Spice Fire"]
    addToppings = ["", "", "", ""]
    toppingCost = 3

    toppings = input(("Toppings ($3) (enter y or n): "))

    if toppings == 'y':
        for i in range(len(toppingsList)):
            addToppings[i] = input(f"Would you like {toppingsList[i]}: ")

            if addToppings[i] == 'y':
                bill += toppingCost

    return bill

print("Welcome to Palpatine Pizzeria!")
size = input(f"What size pizza would you like? S(${smallPizza}), M(${mediumPizza}), or L(${largePizza}): ")

if size == 'S':
    bill = smallPizza
    totalBill = toppings(bill)
elif size == 'M':
    bill= mediumPizza
    totalBill = toppings(bill)
elif size == 'L':
    bill = largePizza
    totalBill = toppings(bill)
else:
    print("Enter the correct size.")

print(f"Your total bill is ${totalBill}")
