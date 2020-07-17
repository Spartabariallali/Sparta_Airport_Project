import pandas as pd
import time
from database.create_connection import Database_OOP

import csv


economy = { "econ_one_way": {"Paris":60,
                                "Madrid":75,
                                "Barcelona":78,
                                "Munich":80,
                                "Rome":90,
                                "Milan":120,
                                "Lisbon":80,
                                "Amsterdam":65,
                                "New York": 230,
                                "Tokyo": 450},

                "econ_return": {"Paris":100,
                                "Madrid":140,
                                "Barcelona":130,
                                "Munich":150,
                                "Rome":160,
                                "Milan":230,
                                "Lisbon":170,
                                "Amsterdam":110,
                                "New York": 396,
                                "Tokyo": 830}}

df_econ = pd.DataFrame({ "Economy OneWay": {"Paris":60,
                                "Madrid":75,
                                "Barcelona":78,
                                "Munich":80,
                                "Rome":90,
                                "Milan":120,
                                "Lisbon":80,
                                "Amsterdam":65,
                                "New York": 230,
                                "Tokyo": 450},

                "Economy Round Trip": {"Paris":100,
                                "Madrid":140,
                                "Barcelona":130,
                                "Munich":150,
                                "Rome":160,
                                "Milan":230,
                                "Lisbon":170,
                                "Amsterdam":110,
                                "New York": 396,
                                "Tokyo": 830}})


business = {"Business One Way":{"Paris":120,
                                    "Madrid":140,
                                    "Barcelona":110,
                                    "Munich":130,
                                    "Rome":115,
                                    "Milan":160,
                                    "Lisbon":110,
                                    "Amsterdam":100,
                                    "New York": 350,
                                    "Tokyo": 560},

                "Business Round Trip": {"Paris":350,
                                    "Madrid":300,
                                    "Barcelona":320,
                                    "Munich":290,
                                    "Rome":380,
                                    "Milan":300,
                                    "Lisbon":280,
                                    "Amsterdam":180,
                                    "New York":550,
                                   "Tokyo":990}}




df_business = pd.DataFrame({"Business One Way":{"Paris":120,
                                    "Madrid":140,
                                    "Barcelona":110,
                                    "Munich":130,
                                    "Rome":115,
                                    "Milan":160,
                                    "Lisbon":110,
                                    "Amsterdam":100,
                                    "New York": 350,
                                    "Tokyo": 560},

                "Business Round Trip": {"Paris":350,
                                    "Madrid":300,
                                    "Barcelona":320,
                                    "Munich":290,
                                    "Rome":380,
                                    "Milan":300,
                                    "Lisbon":280,
                                    "Amsterdam":180,
                                    "New York":550,
                                   "Tokyo":990}})





# print(df_econ)
# print(df_business)




"""
And what class will you be travelling with today...
if class == economy then show the economy options and visa versa
Then ask would you be travelling one way or would you like a return flight
if way_trip == oneway show the one way option and visa versa
Please choose one of these lovely destinations you would like to visit
based on the above code we will know whether to show the price for a which class
and which way trip for someone going to (france e.g)
"""

"""
import translation module, based off of the country they pick we can add some translation
"""




class Choose_destination():
    def price_checker(self):
        booking_info = []
        print("Thank you for choosing AgileAirlines as your provider, we will now tak you to the flight interface: ")
        print("One moment please... Your holiday of a lifetime awaits!!")
        time.sleep(3)
        print("---> Business [B]\n", "---> Economy [E]\n")
        seat_class = input("What class would you like to fly on? \n").upper()
        if seat_class == "B":
            print(df_business, "\n")
            seat_class = "Business"
            booking_info.append(seat_class)
            print("Here is a list of all current flights available at Business Class\n")
            print("Please now select what City you would like to travel to and whether you would like a One Way or Round Trip\n")
            way_trip = input("Type [OW] for one way, [RT] for round trip: \n").upper()
            if way_trip == "OW":
                way_trip = "Business One Way"
                booking_info.append(way_trip)
            elif way_trip == "RT":
                way_trip = "Business Round Trip"
                booking_info.append(way_trip)
            city = input("Please type the city the way it appears in the above table \n")
            booking_info.append(city)
            print("You have chosen the {} ticket and the city is  {}".format(way_trip, city))
            print("The price per Adult for this journey would be -->"), print(business[way_trip][city])
            proceed = input("Are you happy to proceed? Please type yes or no ").upper()
            if proceed == "YES":
                booking_info.append(business[way_trip][city])
            else:
                print("Ohh that's a shame!, we will now take you back to the main menu...")
                return False

        elif seat_class == "E":
            print(df_econ, "\n")
            seat_class = "Economy"
            booking_info.append(seat_class)
            print("Here is a list of all current flights available at Economy Class\n")
            print("Please now select what City you would like to travel to and whether you would like a One Way or Round Trip\n")
            way_trip = input("Type [OW] for one way, [RT] for round trip: \n").upper()
            if way_trip == "OW":
                way_trip = "econ_one_way"
                booking_info.append(way_trip)
            elif way_trip == "RT":
                way_trip = "econ_return"
                booking_info.append(way_trip)
            city = input("Please type the city the way it appears in the above table \n")
            booking_info.append(city)
            print("You have chosen the {} ticket and the city is {}\n".format(way_trip, city))
            print("The price per Adult for this journey would be -->"), print(economy[way_trip][city])
            booking_info.append(economy[way_trip][city])
            passengers = int(input("How many adults would you be booking for today?\n "))
            booking_info.append(passengers)
            print("Give us a moment, we're just calculating your price...\n")
            time.sleep(3)
            ticket_price = economy[way_trip][city]
            total_price = (ticket_price * passengers)
            proceed = input("The total booking price would be {}. Are you happy to proceed? Please type yes or no\n".format(total_price)).upper()
            print("Checking Variable -->", proceed)
            if proceed == "YES":
                booking_info.append(total_price)
                print(booking_info)
                time.sleep(10)
                print("Great! Adding the flight details to our database, we will now need some personal information")
                # run the query here for the flights table
                object1 = Database_OOP()
                cursor1 = object1.establish_connection()
                # query2 = """ INSERT INTO [Flights](flight_destination)
                #             VALUES
                #             (?) """
                # values = (booking_info[2])
                # cursor1.execute(query2, values)
                # cursor1.commit()
                # cursor1.close()
                # object2 = Database_OOP()
                # cursor2 = object2.establish_connection()
                # Now are running a query for the booking table
                with open('booking_information.csv', mode='w') as booking_file:
                    booking_write = csv.writer(booking_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    booking_write.writerow(booking_info)
                query3 = """ INSERT INTO [Bookings](booking_class, booking_way_trip, booking_destination,
                                                    booking_price_per_passenger, booking_no_of_passengers,
                                                    booking_total_fare)
                            VALUES
                            (?, ?, ?, ?, ?, ?)"""
                print(booking_info)
                values = (booking_info[0], booking_info[1], booking_info[2], booking_info[3], booking_info[4], booking_info[5])
                cursor1.execute(query3, values)
                cursor1.commit()


                print("Changing Interface, One moment...")
                time.sleep(2)
            else:
                print("Ohh that's a shame!, we will now take you back to the main menu...")
                return False
        print(booking_info)
        return booking_info












# how to access price from a nested dictionary print business[businessoneway]["Paris"]


"""
Ask how many passengers this will be for
After this is done begin filling up the plane with passengers
"""

# num_of_tickets = int(input("How many tickets would you like to purchase:\n"))
# tickets = range(1,num_of_tickets+1)
# if num_of_tickets in tickets:
#         print("you are about to purchase {} tickets".format(num_of_tickets))


"""
destination = pd.DataFrame({"Destination":{"France":"Paris",
                                "Spain":"Madrid",
                                "Spain":"Barcelona",
                                "Germany":"Munich",
                                "Italy":"Rome",
                                "Italy":"Milan",
                                "Portugal":"Lisbon",
                                "Netherlands":"Amsterdam",
                                "America":"New York",
                                "Japan":"Tokyo"}})


print(destination)
"""

