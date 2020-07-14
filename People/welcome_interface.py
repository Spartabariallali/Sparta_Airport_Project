
class Welcome_interface():

    def user_interaction_passengers(self):

        print("\n*** Airport Assistant Passenger Booking Interface ***")
        assistant_first_name = str(input("Please enter your name: \n")).title()
        print("Hello {}, what service does the passenger require: \n".format(assistant_first_name))
        user_help = "\nInstructions:\n\n" + "-> Create a new booking [T]\n" + "-> view an existing booking [S]\n" +\
                         "-> Amend an existing booking [E]\n" + "-> View Terms & Conditions of booking [H]\n" + "-> Count down to booking [A]\n" +\
                            "-> For help type [H]\n"
        print(user_help)

