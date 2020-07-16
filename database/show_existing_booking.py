import time
from create_connection import Database_OOP


class Show_existing_booking():

    def existing_booking_query(self):
        obj1 = Database_OOP()
        cursor = obj1.establish_connection()
        flight_id = input("Please input your FlightID: ")
        print("One moment please... Loading your booking details!")
        time.sleep(3)
        query = "SELECT * FROM Flights WHERE FlightID = {} ".format(flight_id)
        cursor.execute(query)
        print("Below are your flight details: \n", query)
        back = input("Would you like to return to the main menu for additional services? [YES] [N0] ").upper()
        if back == "YES":
            return
        else:
            print("Thank you for using Agile Airlines!")
        # cursor.commit()
