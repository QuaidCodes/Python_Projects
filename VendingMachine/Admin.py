
from VendingMachine import VendingMachine


# admin has rights to delete, add, and close vending machine, change prices.
class Admin(VendingMachine):
    valid_admins = ["quaidtahir", "admin"]

    def choices(self):
        choice = -7

        while choice != 0:
            self.admin_interface()
            choice = input("Choose: ")

        return 0

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