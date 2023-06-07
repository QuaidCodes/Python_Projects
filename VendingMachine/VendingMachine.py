

class VendingMachine:
    funds = 0
    choice = 0
    cart = []

    def __init__(self, funds=0, choice=0):
        self.funds = funds
        self.choice = choice

    row1 = ("Mango", "Apples", "Grapes")
    row2 = ("Pepsi", "Sprite", "CocaCola")
    row3 = ("Hershey", "Kitkat", "Snickers")
    row4 = ("Cheetos", "Potato Chips", "Takis")
    row5 = ("Onions", "Tomatoes", "Corn")

    selection = (row1, row2, row3, row4, row5)  # Multidimensional list of tuples

    # Vending Machine Functions
    def show_selections(self):
        for i in range(len(self.selection)):
                print(self.selection[i])
        print(self.cart)

    # Features for User
    def add_cart(self):
        pass
        # Show Selection List & User cart & Funds
    def remove_cart(self):
        pass
        # Show selection List & User Selections & Funds
    def purchase(self):
        pass
    def cancel(self):
        pass

