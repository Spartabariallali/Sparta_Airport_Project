import time
from Airport.destination_and_price import Choose_destination
# from welcome_interface import Welcome_interface
from deleting_passenger_info_from_database import Deleting_passenger_info
from show_existing_booking import Show_existing_booking
from adding_passenger_info_to_database import Adding_passenger_info
# Now I need to ask the passenger where they would like to fly to


class Menu_interface():
    def create_booking(self):
        object1 = Choose_destination()
        object1.price_checker()
        # Before this part I want to add their flights and their ticket prices
        obj1 = Adding_passenger_info()
        obj1.storing_passenger_info()


    def amend_existing_booking(self):
        user_help = "\nInstructions:\n\n" + "-> Change Booking time [T]\n" + "-> Cancel booking [C]\n" + "-> Go back [B]\n"
        print(user_help)
        booking_change = input("What part of your booking would you like to amend? ").upper()
        if booking_change == "C":
            object1 = Deleting_passenger_info()
            object1.delete_info()
        elif booking_change == "T":
            pass # I will need to make some sort of class that can change booking times and have the times of flights
        elif booking_change == "B":
            return
            # obj1 = Welcome_interface()
            # obj1.user_interaction_passengers()

    def view_existing_booking(self):
        obj1 = Show_existing_booking()
        obj1.existing_booking_query()
        # booking_id = input("Please input your bookingID: ")
        # print("One moment please... Loading your booking details!")
        # time.sleep(3)
        # I would need to run a query that selects the booking info
        # I would need to use joins to select Passenger IDs e.g. where booking_ID == n
