
from VendingMachine import VendingMachine


# admin has rights to delete, add, close vending machine, and change prices.
# admin also has access to the stored funds
class Admin(VendingMachine):

    def __init__(self):
        self.valid_admins = ["quaidtahir", "admin"]
        self.funds = 0

    def __del__(self):
        ...

    def choices(self):
        choice = -7

        while choice != 0:
            self.admin_interface()
            choice = input("Choose: ")

    def add_selection(self):
        pass

    def remove_selection(self):
        pass

    def shutdown(self):
        pass

    def start(self):
        pass

    def exit(self):
        pass

    def sales(self):
        self.funds += 0

    def admin_interface(self):
        print("1. Selection List\n2. Remove\n3. Add\n4. Start\n5. Shutdown\n0. Exit")
        user_selection = int(input())

        if user_selection == 1:
            self.show_selections()
            self.admin_interface()

        elif user_selection == 2:
            self.remove_selection()
            self.show_selections()
            self.admin_interface()

        elif user_selection == 3:
            self.add_selection()
            self.show_selections()
            self.admin_interface()

        elif user_selection == 4:
            self.start()
            self.show_selections()
            self.admin_interface()

        elif user_selection == 5:
            self.shutdown()

        elif user_selection == 0:
            self.exit()

        else:
            print("Invalid choice!")