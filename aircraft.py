
class Aircraft():  # create a class of Aircraft
    def __init__(self, model, airline):
        self.model = model
        self.airline = airline

class Long_Haul(Aircraft):  # create a long_haul for flights over 3000km
    def __init__(self, model, airline, capacity, num_rows, num_seats_per_row):
        super().__init__(model, airline)
        self.capacity = capacity  # capacity will include the crew
        self.num_rows = num_rows  # number of rows for passengers
        self.num_seats_per_row = num_seats_per_row  # number of seats across each row

    def seating_plan(self):  # returns allowed rows and seats as a tuple
        return (range(1, self.num_rows + 1), "ABCDEFGHJK" [:self.num_seats_per_row])
    
    def capacity(self,passenger_capacity = 0):
        self.passenger_capacity = passenger_capacity
        capcity_empty = passenger_capacity
        for i in passneger_manifest:
            passenger_capacity -= 1

# this produces a range object which is used as an iterable series of row numbers. The slice method returns
# a string with one character per seat


class Short_Haul(Aircraft):  # create a short_haul for flights under 2999km
    def __init__(self, model, airline, capacity, num_rows, num_seats_per_row):
        super().__init__(model, airline)
        self.capacity = capacity  # capacity will include the crew
        self.num_rows = num_rows  # number of rows for passengers
        self.num_seats_per_row = num_seats_per_row  # number of seats across each row

    def seating_plan(self):  # returns allowed rows and seats as a tuple
        return (range(1, self.num_rows + 1), "ABCDEF" [:self.num_seats_per_row])


pa747 = Long_Haul("Boeing", "PythonAir", 263, 25, 10)  # creating an instance of a long haul with 250 passengers and 13 crew
aa220 = Short_Haul("Airbus", "AgileAir", 113, 18, 6)  # creating an instance of a short haul with 108 passengers and 5 crew
print(pa747.seating_plan())  # (range(1, 26), 'ABCDEFGHJK') (half open range)
print(aa220.seating_plan())  # (range(1, 19), 'ABCDEF')


capacity = 300 


passenger_list = [("bar","allali",27),("andrew","osbourne",30),("agbo","lamina",16),("georgina","barteltt",29)]

for i in passenger_list:
  capacity -= 1

print(capacity)











# class Helicopter(Aircraft):
#     def __init__(self, model, airline, capacity, num_seats):
#         super().__init__(model, airline)
#         self.capacity = capacity
#         self.num_seats = num_seats
