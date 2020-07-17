## FRONT END INTERFACE README  

#### Menu:  
Created a menu that imports the database functions.  
Options:  
- Create a booking (using the add passenger functions)  
- Amend a booking (using the delete passenger functions)  
- View an existing booking (using the passenger table) 
- Check flight status 

```python
class Menu_interface():
    def create_booking(self):
        obj1 = Adding_passenger_info()
        obj1.storing_passenger_info()
```

#### Welcome:  
Created a welcome screen hosting a series of options for the Airport Assistant to choose from.  
Options:  
- Create a new booking  
- View an existing booking  
- Amend an existing booking  
- View T&Cs  
- Count down to booking  
- Help  

This welcome screen is fed by the Menu Interface

```python
def user_interaction_passengers(self):

    print("\n*** Airport Assistant Passenger Booking Interface ***")
    assistant_first_name = str(input("Please enter your name: \n")).title()
```