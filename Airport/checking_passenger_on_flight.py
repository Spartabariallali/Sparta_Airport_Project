from database.create_connection import Database_OOP


class Checking_passengers:
    def check_passengers(self):
        object1 = Database_OOP()
        cursor = object1.establish_connection()
        ####
        check_seats_on_flight = input("What destination are you flying to? ")
        query = "SELECT * FROM Aircraft WHERE destination = '{}'".format(check_seats_on_flight)
        # Run a query that subtracts the capacity by the number of passenger IDs assigned to that flight
        # To be done tomorrow
        results = cursor.execute(query)
        for row in results:
            print(row)
        back = input("Would you like to return to the Main interface? [YES] [NO]").upper()
        if back == "YES":
            return


