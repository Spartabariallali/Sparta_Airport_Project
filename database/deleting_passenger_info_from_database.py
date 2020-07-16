import time
from create_connection import Database_OOP
# Potentially create an iteration where if the user cancels their tickets too close to the time of the flight then
# they are only eligible for a voucher


# If they want to cancel, we can ask them for some sort of user feedback that we can put within a .txtfile
# Now be able to cancel remove multiple passengers that may be on the same bookingID, so we should use booking ID instead
class Deleting_passenger_info():
    def delete_info(self):
        print("It's a shame you want to cancel your booking with us...\n")
        feedback = input("Please provide us with some information as to why you have chosen to cancel the booking? \n")
        unique_number = int(input("Finally, please provide us with your PassengerID number that was given to you when you made your booking \n"))
        print("One moment please....")
        time.sleep(2)
        with open("user_feedback.txt", "a+") as file:
            text_input = "\nPassengerID: {} ---> {}".format(unique_number, feedback)
            file.write(text_input)
            # print("\n", "PassengerID: {}".format(unique_number), "--->", file.write(feedback))

        # now time to remove this information from the database
        obj1 = Database_OOP()
        cursor = obj1.establish_connection()
        query = "DELETE FROM Passengers WHERE PassengerID = {}".format(unique_number)
        cursor.execute(query)
        cursor.commit()

        print("Thank you very much for your feedback, your booking details have been removed from our database "
              "and your money should be with you in 3-5 working days, Bye!")




# obj = Deleting_passenger_info()
# obj.delete_info()