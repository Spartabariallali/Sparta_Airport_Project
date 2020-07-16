import time
from people import *

class Flights:
    #  This is a simple method which contains two nested dictionaries
    # Within the dictionaries, I made the distinction between long and short haul flights
    # The distinction is essential to my tactic of assigning my list indexes to the keys of the nested dicts
    def flightRoutes(self, short, long):
        class1 = {short: {"Amsterdam": 357,
                          "Barcelona": 1138,
                          "Lisbon": 1585,
                          "Madrid": 1264,
                          "Milan": 959,
                          "Munich": 940,
                          "Paris": 344,
                          "Rome": 1435}}
        class2 = {long:  {"Tokyo": 9556,
                          "New York": 5572}}
        #  simple list containing dummy planes, will need to implement Georgina's classes to build a more robust app
        planes = ["plane1", "plane2", "plane3", "plane4", "plane5", "plane6", "plane7", "plane8", "plane9", "plane10"]
        #  i assign the short flights to a single plane, and the long flights to another plane
        #  * We should try and work on a way of using multiple planes as more than one of our planes will be operating
        # at a time
        class1[short] = planes[0]
        class2[long] = planes[1]
        new_short = ""
        new_long = ""
        exit = True
        # I used a while loop to restart the process after the assignment has been changed

        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        while exit:
            if username == "manager" and password == "pass1":

                editor = input("Would you like to change a plane assignment y/n? ").lower()
                if editor == "y":
                    change_assignment = input("Press [S] for short haul and [L] for long haul: ").lower()
                    if change_assignment == "s":
                        current_short = input(f"{class1[short]} is currently assigned to this route, would you like to change it y/n? ").lower()
                        if current_short == "y":
                            change_short = input("Which plane would you like assign to this route?\n " + "-> Plane3 [3]\n" +
                                             " -> Plane4 [4]\n" + " -> Plane5 [5]\n" + " -> Plane6 [6]\n ")
                            new_short = change_short
                            print(f"You have chosen to assign Plane{new_short}  to this route")
                            time.sleep(3)
                            confirmation = input("Press [Y] to confirm your selection or [N] to cancel ").lower()
                        if confirmation == "y":
                            print(f"Plane{new_short} has been assigned to this route")
                        elif confirmation == "n":
                            print("All changes have been cancelled")
                            exit = False
                        elif current_short == "n":
                            print("No changes have been made.")
                            self.flightRoutes() # find a way to restart from here


                    elif change_assignment == "l":
                            current_long = input(f"{class2[long]} is currently assigned to this route, would you like to change it y/n? ").lower()
                            if current_long == "y":
                                change_long = input("Which plane would you like assign to this route?\n " + "-> Plane3 [3]\n" +
                                                 " -> Plane4 [4]\n" + " -> Plane5 [5]\n" + " -> Plane6 [6]\n ")

                                new_long = change_long
                                print(f"You have chosen to assign Plane{new_long}  to this route")
                                time.sleep(3)
                            confirmation = input("Press [Y] to confirm your selection or [N] to cancel ").lower()
                            if confirmation == "y":
                                print(f"Plane{new_long} has been assigned to this route")
                            elif confirmation == "n":
                                print("All changes have been cancelled")
                            elif current_long == "n":
                                print("No changes have been made.")
                                exit = False
                            else:
                                print("No worries, have a nice day")
            elif username != "manager" and password != "pass1":
                print("Please check that data is correct")
                break









f1 = Flights()
f1.flightRoutes(short=None, long=None)
