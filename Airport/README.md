## AIRPORT README

#### T&C:  
T&C can be printed to show AgileAirline's T&Cs

```python
class View_terms_and_conditions():
    def run_t_and_c(self):
        with open('1.jpg', "rb") as picture:
            pic = picture.read()
            Image.open("1.jpg").show()
```
#### Booking Flight:  
All flights and prices are stored here and can be booked according to their class.  
If the customer is happy they can the go ahead and enter their personal details to book their flight.  
```python
class Choose_destination():
    def price_checker(self):
        booking_info = []
        print("Thank you for choosing AgileAirlines as your provider, we will now tak you to the flight interface: ")
        print("One moment please... Your holiday of a lifetime awaits!!")
        time.sleep(3)
        print("---> Business [B]\n", "---> Economy [E]\n")
```
#### Checking Passengers:  
Checking passengers are on the flight 
 
```python
class Checking_passengers:
    def check_passengers(self):
        object1 = Database_OOP()
        cursor = object1.establish_connection()
        check_seats_on_flight = input("What destination are you flying to? ")
        query = "SELECT * FROM Flights WHERE flight_destination == {}".format(check_seats_on_flight)
```
