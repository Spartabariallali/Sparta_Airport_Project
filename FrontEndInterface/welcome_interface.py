from menu_interface import Menu_interface
from Airport.terms_and_conditions import View_terms_and_conditions
class Welcome_interface():

    def user_interaction_passengers(self):

        print("\n*** Airport Assistant Passenger Booking Interface ***")
        assistant_first_name = str(input("Please enter your name: \n")).title()
        print("Hello {}, what service does the passenger require: \n".format(assistant_first_name))
        user_help = "\nInstructions:\n\n" + "-> Create a new booking [T]\n" + "-> view an existing booking [S]\n" +\
                         "-> Amend an existing booking [E]\n" + "-> View Terms & Conditions of booking [H]\n" + "-> Count down to booking [A]\n" +\
                            "-> For help type [H]\n"
        print(user_help)
        passenger_input = input("Please select from the options.").upper()
        if passenger_input == 'T':
            obj1 = Menu_interface()
            obj1.create_booking()
        elif passenger_input == "E":
            obj1 = Menu_interface()
            obj1.amend_existing_booking()
        elif passenger_input == "S":
            obj1 = Menu_interface()
            obj1.view_existing_booking()
        elif passenger_input == "H":
            obj1 = View_terms_and_conditions()
            obj1.run_t_and_c()

            pass # Here I am going to read in a picture which contains the terms and conditions for the booking


