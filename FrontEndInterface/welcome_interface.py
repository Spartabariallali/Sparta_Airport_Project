from menu_interface import Menu_interface

class Welcome_interface():

    def user_interaction_passengers(self):

        print("\n*** Airport Assistant Passenger Booking Interface ***")
        assistant_first_name = str(input("Please enter your name: \n")).title()
        print("Hello {}, what service does the passenger require: \n".format(assistant_first_name))
        user_help = "\nInstructions:\n\n" + "-> Create a new booking [T]\n" + "-> view an existing booking [S]\n" +\
                         "-> Amend an existing booking [E]\n" + "-> View Terms & Conditions of booking [H]\n" + "-> Count down to booking [A]\n" +\
                            "-> For help type [H]\n"
        print(user_help)
        passenger_input = input("Please select from the options.")
        if passenger_input == 't':
            obj1 = Menu_interface()
            obj1.create_booking()
        elif passenger_input == "e":
            obj1 = Menu_interface()
            obj1.amend_existing_booking()
        elif passenger_input == "s":
            obj1 = Menu_interface()
            obj1.view_existing_booking()
        elif passenger_input == "h":
            pass # Here I am going to read in a picture which contains the terms and conditions for the booking


