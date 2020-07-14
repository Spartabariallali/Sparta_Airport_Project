# simple classes which will be iterated to take user inputs
class People:
    def __init__(self, f_name, l_name, age, gender, id_number, passport_number ):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.id_number = id_number
        self.passport_number = passport_number

#  subclass of the above that will also take user inputs
class Passenger(People):
    def details(self):
        print(self.f_name + self.l_name + self.age + self.gender + self.id_number + self.passport_number)

class Staff(People):
    def s_details(self):
        print(self.f_name + self.l_name + self.age + self.gender + self.id_number + self.passport_number)

# this was an experiment with passwords and how they work
class Managers(Staff):
    def changes(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")





        if username == "manager" and password == "pass1":
            options = input(f"\nWelcome {self.f_name.title()}, which details would you like to amend? ")
            if options == "amend plane details":
                pass
        elif username != "manager" and password != "pass1":
            print("Please check that data is correct")
        # elif options == "assign a plane to a route":



flight =






        # planes = input("plane1, plane2, plane3 ")



# agbo = Passenger("Agbo ", "Lamina ", "24 ", "male ", "419 ", "NG419")
# agbo.details()
# bari = Staff("bari ", "allali ", "24 ", "male ", "213 ", "fr213")
# bari.s_details()
bob = Managers("bob ", "smith ", " 45 ", "female ", "123 ", "12345 ")
bob.changes()