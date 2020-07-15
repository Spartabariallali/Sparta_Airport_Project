from people import *
# After importing the attributes from people, I created an assistant who is able to log in and will be able to make bookings once they are logged in
class Assistant(Staff):
    def login(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        exit = True

        while exit:
            if username == "assistant" and password == "pass2":
                options = input(f"\nWelcome {self.f_name.title()}, what would you like to do today? ")
                if options == "amend plane details":
                    pass
            elif username != "manager" and password != "pass1":
                print("Incorrect username and/or password")
                self.login()

tim = Assistant("tim", "timson", "3", "male", "54321", "1234")
tim.login()