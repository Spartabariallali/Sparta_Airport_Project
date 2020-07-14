import pyodbc
import time
from create_connection import Database_OOP
from menu_interface import Menu_interface
from welcome_interface import Welcome_interface

"""
In this class we attempt to add the information inputted from the airport assistant to build a database
that holds passenger info
"""

class Adding_passenger_info:
        def storing_passenger_info(self):
            ob1 = Database_OOP()
            cursor = ob1.establish_connection()
            obj2 = Menu_interface()
            time.sleep(1)
            obj3 = Welcome_interface()
            obj3.user_interaction_passengers()
            passenger_info = obj2.create_booking()
            query = """ INSERT INTO [Passengers](title, first_name, last_name, date_of_birth, gender, nationality,
                                                   travel_documentation, travel_doc_number)
                                                   VALUES
                                                   (?, ?, ?, ?, ?, ?, ?, ?) """

            values = (passenger_info[0], passenger_info[1], passenger_info[2], passenger_info[3], passenger_info[4], passenger_info[5], passenger_info[6], passenger_info[7])

            cursor.execute(query, values)
            cursor.commit()

            passengers = cursor.execute("SELECT * FROM Passengers")
            for row in passengers:
                print(row)


object = Adding_passenger_info()
object.storing_passenger_info()