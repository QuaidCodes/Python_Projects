# Gotham Vending Machine
# Take funds and dispense pick

login = str(input("What are your logins: "))

if login == "admin":
    from Admin import Admin

    AdminList = Admin()

    login = str(input("Enter admin logins: "))

    for i in range(len(AdminList.valid_admins)):
        if login == AdminList.valid_admins[i]:
            Admin.choices(AdminList)
        else:
            print("Wrong login/password")
