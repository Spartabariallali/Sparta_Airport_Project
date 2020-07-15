from people import *
# After importing the attributes from people, I created a manager who is able to log in and will be able to use change flight assignments once he has logged in
class Managers(Staff):
    def changes(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        exit = True

        while exit:
            if username == "manager" and password == "pass1":
                options = input(f"\nWelcome {self.f_name.title()}, which details would you like to amend? ")
                if options == "amend plane details":
                    pass
            elif username != "manager" and password != "pass1":
                print("Please check that data is correct")
                self.changes()

bob = Managers("bob ", "smith ", " 45 ", "female ", "123 ", "12345 ")
bob.changes()