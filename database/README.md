## DATABASE README

#### Database:  
Created a database in SQL to hold four tables:  
* Passengers  
* Staff  
* Bookings  
* Aircraft  

#### Connecting to DB:  
Python document created to establish a connection to SQL database  
Establish connection using pyodbc with error handling to deal with connection timing out.  

```python
class Database_OOP:
    server = secret_file.server
    database = secret_file.database
    username = secret_file.username
    password = secret_file.password
```
#### Adding Passengers:  
Once connection is established we can add passengers to the database using the interactive interface.  
This will ask the Airport Assistant to enter the following details:  
* Title  
* First name  
* Last name  
* DOB  
* Gender  
* Choose Identity Card or Passport  
* Identity Card or Passport Number  

This data will then be added to the passengers table in the SQL database  

```python
class Adding_passenger_info:
        def storing_passenger_info(self):
            ob1 = Database_OOP()
            cursor = ob1.establish_connection()
```
#### Removing Passengers:  
After passengers have been added they can also be removed from the database (if they cancel or miss their flight)  
Passenger must provide PassengerID number (created when being added to passenger list) in order to be removed from the system.  
User feedback placed into txt file for reason behind cancellation - any string can be added here.  
  
```python
class Deleting_passenger_info():
    def delete_info(self):
        print("It's a shame you want to cancel your booking with us...\n")
```