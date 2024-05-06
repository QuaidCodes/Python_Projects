class VendingMachine:
    def __init__(self):
        self.funds = 0
        self.choice = 0
        self.cart = []

        # Multidimensional list of tuples (Possible create a JSON file containing key value pairs for cost and item)
        self.selection = [
            ["Mango", "Apples", "Grapes"],
            ["Cashews", "Almonds", "Peanuts"]
        ]

    def __del__(self):
        ...

    def landing(self):
        self.interface()

    # Funds validation and initialization
    def funds_setter(self):
        condition = True

        while condition:
            self.funds = int(input("Insert $1, $5, or $10 bills only: "))

            if self.funds_getter() > self.total_cost_getter():
                print("You are too rich to purchase from us. Are you really from Gotham?! Insert less money.")
            else:
                condition = False

    def funds_getter(self):
        return self.funds

    # Returns gross value of products in the vending machine
    def total_cost_getter(self):
        return 10

    # Vending Machine Functions
    def interface(self):
        print("----- ------ -------- -----")
        print("----- Gotham Vendings -----")
        for i in range(len(self.selection)):
            print(self.selection[i])
        print("----- ------ -------- -----")

        print("1. Add, 2. Remove, 3. Buy, 4. View Cart, 0. Cancel")

        vending_function = int(input(""))

        # Adds an item in the vending machine to the cart and subtracts from inventory
        if vending_function == 1:
            self.add_item()

        # Removes/Pops an item from cart
        elif vending_function == 2:
            self.remove_item()

        # Lets the user checkout and displays total
        elif vending_function == 3:
            self.buy()

        elif vending_function == 4:
            self.show_cart()
        # clear the current inventory
        elif vending_function == 0:
            self.cancel()

    # Features for User
    # Add an item to the cart list from selection list
    def add_item(self):
        column = int(input("Pick an item\nColumn: "))
        row = int(input("Row: "))

        self.cart.append(self.selection[column][row])
        self.interface()

    # Show Selection List & User cart & Funds
    def remove_item(self):
        pass

    def show_cart(self):
        if len(self.cart) > 0:
            for i in self.cart:
                if self.cart.index(i) == len(self.cart):
                    print(i)
                else:
                    print(i, end='')
        else:
            print("Your cart is empty.")

    # Show selection List & User Selections & Funds
    def buy(self):
        print(f"Your total is {len(self.cart)}")
        self.cart.clear()

    # Clear cart list
    def cancel(self):
        self.cart.clear()

