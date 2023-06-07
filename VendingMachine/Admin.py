
from VendingMachine import VendingMachine


# admin has rights to delete, add, and close vending machine.
class Admin(VendingMachine):
    valid_admins = ["quaidtahir"]

    def choices(self):
        choice = 5

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

    @staticmethod
    def admin_interface():
        print("1. See Selection List\n2. Remove\n3. Shutdown\n4. Start\n5. Add\n0. Exit")
