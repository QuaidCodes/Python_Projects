class VendingMachine:
    funds = 0
    choice = 0
    cart = ["Onions"]

    def __init__(self, funds=0, choice=0):
        self.funds = funds
        self.choice = choice

    # Make the strings all equal length by adding extra space
    row1 = ("Mango", "Apples", "Grapes")
    row2 = ("Pepsi", "Sprite", "CocaCola")
    row3 = ("Hershey", "Kitkat", "Snickers")
    row4 = ("Cheetos", "Potato Chips", "Takis")
    row5 = ("Onions", "Tomatoes", "Corn")

    selection = [row1, row2, row3, row4, row5]  # Multidimensional list of tuples

    # Vending Machine Functions
    def show_selections(self):
        for i in range(len(self.selection)):
            print(self.selection[i])

        print("1. Add, 2. Remove, 3. Buy, 4. Cancel, 5. View Cart")

        vending_function = int(input(""))

        if vending_function == 1:
            i1 = int(input("Index 1: "))
            i2 = int(input("Index 1: "))
            self.add_item(i1, i2)

        elif self == 2:
            self.remove_item()

        elif self == 3:
            self.buy()

        else:
            self.cancel()

    # Features for User
    def add_item(self, i, j):
        self.cart.append(list(self.selection[i][j]))

    # Show Selection List & User cart & Funds
    def remove_item(self):
        pass

    # Show selection List & User Selections & Funds
    def buy(self):
        print(f"Your total is {len(self.cart)}")
        self.cart.clear()

    def cancel(self):
        self.cart.clear()

    @staticmethod
    def total(this_list):
        return sum(this_list)