
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




# class Helicopter(Aircraft):
#     def __init__(self, model, airline, capacity, num_seats):
#         super().__init__(model, airline)
#         self.capacity = capacity
#         self.num_seats = num_seats
