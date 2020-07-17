import time
from Dbase.dbconnection import OpenConnection
from database.create_connection import Database_OOP


class Flights:
    #  This method contains the loop which runs my user interface
    def flightRoutes(self):
        # Here, I am creating a condition in which my loop will run indefinitely
        exit = True
        # I used a while loop to restart the process after the assignment has been changed
        # these variables are a simple way of creatng a password to gain access to the interface
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        while exit:
            if username == "manager" and password == "pass1":

                editor = input("Would you like to change a plane assignment y/n? ").lower()
                if editor == "y":
                    obj1 = OpenConnection()
                    obj1.connections()
                    time.sleep(2)
                    id_change = input("What PlaneID are you trying to assign? ")
                    destination_change = input("Which destination would you like to assign this PlaneID to? ")
                    confirmation = input(f"You have chosen to assign {id_change} to {destination_change}.\n"
                                         f"Press [Y] to confirm or [N] to decline: ")
                    if confirmation == "y":
                        var1 = """UPDATE Aircraft SET
                        AircraftID = ('{}')
                        WHERE destination IN ('{}')""".format(id_change, destination_change)
                        # values = id_change
                        obj2 = Database_OOP()
                        cursor1 = obj2.establish_connection()
                        cursor1.execute(var1)
                        cursor1.commit()
                    elif confirmation == "n":
                        print("All changes have been cancelled.")
            elif username != "manager" and password != "pass1":
                print("Please check that data is correct")
            elif username != "manager" or password != "pass1":
                print("Please check that data is correct")
            exit = False
            return

