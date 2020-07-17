## AIRPORT README

#### :  
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
#### Removing Passengers:  
After passengers have been added they can also be removed from the database (if they cancel or miss their flight)  
Passenger must provide PassengerID number (created when being added to passenger list) in order to be removed from the system.  
User feedback placed into txt file for reason behind cancellation - any string can be added here.  
  
```python
```
