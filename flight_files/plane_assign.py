import time
from people import *
from Dbase import dbconnection

class Flights:
    #  This is a simple method which contains two nested dictionaries
    # Within the dictionaries, I made the distinction between long and short haul flights
    # The distinction is essential to my tactic of assigning my list indexes to the keys of the nested dicts
    def flightRoutes(self):

        fra = {"France": "Paris"}
        esp = {"Spain": "Barcelona"}
        ger = {"Germany": "Munich"}
        ita = {"Italy": "Rome"}
        ita2 = {"Italy": "Milan"}
        por = {"Portugal": "Lisbon"}
        ned = {"Netherlands": "Amsterdam"}
        usa = {"America": "New York"}
        jap = {"Japan": "Tokyo"}

        #  simple list containing dummy planes, will need to implement Georgina's classes to build a more robust app
        planes = ["plane1", "plane2", "plane3", "plane4", "plane5", "plane6", "plane7", "plane8", "plane9", "plane10"]
        #  i assign the short flights to a single plane, and the long flights to another plane

        fra["France"] = planes[0]
        esp["Spain"] = planes[1]
        ger["Germany"] = planes[2]
        ita["Italy"] = planes[3]
        ita2["Italy"] = planes[4]
        por["Portugal"] = planes[5]
        ned["Netherlands"] = planes[6]
        usa["America"] = planes[7]
        jap["Japan"] = planes[8]
        new_short = ""
        new_long = ""
        exit = True
        # I used a while loop to restart the process after the assignment has been changed

        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        while exit:

            def username_check(self, sql_command, connection, user_input):
                cursor = self.create_cursor(connection)
                query_result = cursor.execute(sql_command)  # (SELECT * FROM PRODUCTS)
                try:
                    if user_input == 1:
                        self.fetch_one(query_result)
                    elif user_input == 2:
                        self.fetch_many(query_result)
                    elif user_input == 3:
                        self.fetch_all(query_result)
                    # elif user_input == 4:
                    # self.avg(query_result)
                    else:
                        raise ValueError
            if username == "manager" and password == "pass1":

                editor = input("Would you like to change a plane assignment y/n? ").lower()
                if editor == "y":
                    current_assignments = input("Here are the current plane assignments:\n\n" +
                                                "Destinations:    Planes:\n" + "Paris           Plane1\n"
                                              + "Madrid          Plane2\n" + "Barcelona       Plane3\n" +
                                                "Munich          Plane4\n" + "Rome            Plane5\n"
                                                + "Milan           Plane6\n" + "Lisbon          Plane7\n"
                                                + "Amsterdam       Plane8\n" + "New York        Plane9\n" +
                                                "Please select the destination you would like to reassign: ")
                    if current_assignments == f"{current_assignments}":
                        print(f"You have chosen to amend {current_assignments}")
                        time.sleep(3)
                        new_plane = input("Which plane would you like to assign to this flight instead? \n " +
                                                 "-> Plane3 [3]\n" + " -> Plane4 [4]\n" + " -> Plane5 [5]\n" +
                                                 " -> Plane6 [6]\n" + " -> Plane7 [7]\n" + " -> Plane8 [8]\n"
                                                 + " -> Plane9 [9]\n" + " -> Plane10 [10]\n ")
                        print(f"You have chosen Plane {new_plane}")
                        confirmation = input("Press [Y] to confirm your selection or [N] to cancel ").lower()
                        if confirmation == "y":
                            print(f"Plane{new_plane} has been assigned to this route")
                        elif confirmation == "n":
                            print("All changes have been cancelled")
                    else:
                     print("No worries, have a nice day")
                     break
            elif username != "manager" and password != "pass1":
                print("Please check that data is correct")
            elif username != "manager" or password != "pass1":
                print("Please check that data is correct")
            exit = False
            self.flightRoutes()

            f1 = Flights()
            f1.flightRoutes()

            #         change_assignment = input("Press [S] for short haul and [L] for long haul: ").lower()
            #
            #
            #         if change_assignment == "s":
            #             current_short = input(f"{class1[short]} is currently assigned to this route, would you like to change it y/n? ").lower()
            #             if current_short == "y":
            #                 change_short = input("Which plane would you like assign to this route?\n " +
            #                                      "-> Plane3 [3]\n" + " -> Plane4 [4]\n" + " -> Plane5 [5]\n" +
            #                                      " -> Plane6 [6]\n" + " -> Plane7 [7]\n" + " -> Plane8 [8]\n"
            #                                      + " -> Plane9 [9]\n" + " -> Plane10 [10]\n")
            #                 new_short = change_short
            #                 print(f"You have chosen to assign Plane{new_short}  to this route")
            #                 time.sleep(3)
            #                 confirmation = input("Press [Y] to confirm your selection or [N] to cancel ").lower()
            #             if confirmation == "y":
            #                 print(f"Plane{new_short} has been assigned to this route")
            #             elif confirmation == "n":
            #                 print("All changes have been cancelled")
            #                 exit = False
            #             elif current_short == "n":
            #                 print("No changes have been made.")
            #             # find a way to restart from here
            #
            #
            #         elif change_assignment == "l":
            #                 current_long = input(f"{class2[long]} is currently assigned to this route, would you like to change it y/n? ").lower()
            #                 if current_long == "y":
            #                     change_long = input("Which plane would you like assign to this route?\n " +
            #                                      "-> Plane3 [3]\n" + " -> Plane4 [4]\n" + " -> Plane5 [5]\n" +
            #                                      " -> Plane6 [6]\n" + " -> Plane7 [7]\n" + " -> Plane8 [8]\n"
            #                                      + " -> Plane9 [9]\n" + " -> Plane10 [10]\n")
            #
            #                     new_long = change_long
            #                     print(f"You have chosen to assign Plane{new_long}  to this route")
            #                     time.sleep(3)
            #                 confirmation = input("Press [Y] to confirm your selection or [N] to cancel ").lower()
            #                 if confirmation == "y":
            #                     print(f"Plane{new_long} has been assigned to this route")
            #                 elif confirmation == "n":
            #                     print("All changes have been cancelled")
            #                 elif current_long == "n":
            #                     print("No changes have been made.")
            #                     exit = False
            #     else:
            #         print("No worries, have a nice day")
            #         break
            # elif username != "manager" and password != "pass1":
            #     print("Please check that data is correct")
            #     exit = False
            #     self.flightRoutes(short=None, long=None)

    def password_check(self):

