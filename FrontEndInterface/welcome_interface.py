from menu_interface import Menu_interface
from Airport.terms_and_conditions import View_terms_and_conditions
from database.check_passenger_database import Check_all_passengers
class Welcome_interface():


    # Find a way so they don't re input name
    def user_interaction_passengers(self):

        print("\n*** Airport Assistant Passenger Booking Interface ***")
        assistant_first_name = str(input("Please enter your name: \n")).title()
        print("Hello {}, what service does the passenger require: \n".format(assistant_first_name))
        user_help = "\nInstructions:\n\n" + "-> Create a new booking [C]\n" + "-> view an existing booking [E]\n" +\
                         "-> Amend an existing booking [A]\n" + "-> View Terms & Conditions of booking [T]\n" + "-> Check Passenger Database [P]\n" +\
                            "-> For help type [H]\n"
        print(user_help)
        passenger_input = input("Please select from the options: ").upper()
        if passenger_input == 'C':
            obj1 = Menu_interface()
            obj1.create_booking()
            self.user_interaction_passengers()
        elif passenger_input == "A":
            obj1 = Menu_interface()
            obj1.amend_existing_booking()
            self.user_interaction_passengers()
        elif passenger_input == "E":
            obj1 = Menu_interface()
            obj1.view_existing_booking()
            self.user_interaction_passengers()
        elif passenger_input == "T":
            obj1 = View_terms_and_conditions()  # Here I am going to read in a picture which contains the terms and conditions for the booking
            obj1.run_t_and_c()
            self.user_interaction_passengers()
        elif passenger_input == "H":
            pass
        elif passenger_input == "P":
            obj1 = Check_all_passengers()
            obj1.all_passsengers()
            self.user_interaction_passengers()



