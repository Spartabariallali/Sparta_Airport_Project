from aircraft import *

f = Aircraft

class Flight:
    def __init__(self, destination, origin, distance):
        self.destination = destination
        self.origin = origin
        self.distance = distance

    def flight_info(self):

# print(type(f))

pa747 = Long_Haul("Boeing", "PythonAir", 263, 25, 10)  # creating an instance of a long haul with 250 passengers and 13 crew
aa220 = Short_Haul("Airbus", "AgileAir", 113, 18, 6)  # creating an instance of a short haul with 108 passengers and 5 crew
print(pa747.seating_plan())  # (range(1, 26), 'ABCDEFGHJK') (half open range)
print(aa220.seating_plan())  # (range(1, 19), 'ABCDEF')

distance = {"Amsterdam": 357, "Barcelona": 1138, "Berlin": 579, "Lisbon": 1585, "Madrid": 1264, "Milan": 959, "Munich": 940, "New York": 5572, "Paris": 344, "Rome": 1435, "Tokyo": 9556}