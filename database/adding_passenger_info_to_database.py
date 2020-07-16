import time
from create_connection import Database_OOP
import random
# from menu_interface import Menu_interface
# from welcome_interface import Welcome_interface


"""
Try and Exceptions !!!
"""

"""
In this class we attempt to add the information inputted from the airport assistant to build a database
that holds passenger info
"""

"""

"""


class Adding_passenger_info:
        def storing_passenger_info(self):
            ob1 = Database_OOP()
            cursor = ob1.establish_connection()
            passenger_information = []
            print("one moment please...")
            time.sleep(1)
            loops = int(input("Please enter the number of Passengers you have chosen to book with: "))
            i = 0
            for n in range(loops):
            # while i < loops:
                time.sleep(1)
                print("\nPlease follow the prompts and ensure the information is carefully inputted.\n")
                p_title = input(
                    ("Please enter the passenger's title of courtesy: (as it appears on the travel document: \n "))
                passenger_information.append(p_title)
                # first_name_confirmation = str(input("would you like to continue with the first name: {}\n (y/n)".format(passenger_first_name))
                p_first_name = str(input(
                    "Please enter the passenger's first name: (as it appears on the travel document) \n")).title()
                passenger_information.append(p_first_name)
                # last_name
                p_last_name = str(input(
                    "Please enter the passenger's last name: (as it appears on the travel document) \n")).title()
                passenger_information.append(p_last_name)
                # dob
                p_dob = input("Please enter the passenger's date of birth: (yyyy/mm/dd format) \n")
                passenger_information.append(p_dob)
                # gender
                # print("\nMale")
                # print("Female\n")
                # p_gender = str(input("please select the passenger's gender: \n")).lower()
                # if p_gender == 'male':
                #     passenger_information.append("Male")
                # else:
                #     passenger_information.append("Female")
                # nationality
                p_nationality = str(input("Please confirm the passenger's nationality: \n")).title()
                passenger_information.append(p_nationality)
                # passport/travel document
                # print("\n** Passport")
                # print("** National Identity Card (Only Valid for European Travel)\n")
                # p_travel_document = str(input("please confirm the passenger's travel document: \n")).lower()
                # if p_travel_document == 'passport':
                #     passenger_information.append("passport")
                # else:
                #     passenger_information.append("National Identity Card")
                # travel document numbers
                p_travel_document_number = int(input("please enter the passenger's 10 digit travel document number: \n"))
                passenger_information.append(p_travel_document_number)
                print(passenger_information)
                ###
                # return passenger_information
                # all_passengers.append(passenger_information)
                query = """ INSERT INTO [Passengers](title, first_name, last_name, birthdate, nationality,
                                                       travel_doc)
                                                       VALUES
                                                       (?, ?, ?, ?, ?, ?) """

                values = (passenger_information[0], passenger_information[1], passenger_information[2], passenger_information[3], passenger_information[4], passenger_information[5])

                cursor.execute(query, values)
                cursor.commit()

                passenger_information = []
                if n == 2:
                    break

                # start_again = input("Type [Yes] if you would like to enter additional info for another passenger: ").upper()
                #
                # if start_again == "YES":
                #     self.storing_passenger_info()
                # else:
                #     return
            ## Here we run the query to give a booking_id

            random_booking_id = random.randint(161, 500)
            print(random_booking_id)
            print("Your booking ID is: {}".format(random_booking_id))
            query1 = """ UPDATE [Passengers]
                        SET booking_id = (?)
                        WHERE booking_id is NULL 
                            """
            values2 = random_booking_id
            cursor.execute(query1, values2)
            cursor.commit()

            """
            UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
            """