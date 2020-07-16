from database.create_connection import Database_OOP


class Checking_passengers:
    def check_passengers(self):
        object1 = Database_OOP()
        cursor = object1.establish_connection()
        check_seats_on_flight = input("What destination are you flying to? ")
        query = "SELECT * FROM Flights WHERE flight_destination == {}".format(check_seats_on_flight)
        results = cursor.execute(query)
        cursor.commit()
        # rows = cursor.execute(query_result)
        for row in results:
            print(row)
        back = input("Would you like to return to the Main interface? [YES] [NO]").upper()
        if back == "YES":
            return


