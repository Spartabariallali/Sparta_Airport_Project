# Shared Repository for those in Group 3 working on the Airport Project  
## Project following completion of SQL and Python weeks of the DevOps Stream at [Sparta Global](https://www.spartaglobal.com/) 

:airplane: :airplane: :airplane: :airplane:

[Abdelbari](https://github.com/Spartabariallali)  
[Saheed](https://github.com/sahlamina)  
[Georgina](https://github.com/gia-bartlett)  
[Andrew](https://github.com/aosborne17)

It would make sense to first create a database in which we would store various information, that way we can then
run code that can add to and take from that database.


## Airport Project Epic:  
Airport Assistant interface for managing flight bookings and flight manifests.  

## User Stories:  
- Create a passengers list with name and passport number to add to flight  
- Create flight trip with specific destination  
- Assign and change a plane to a flight trip using a password  
- Sell tickets to passengers and add them to flight trip  
- Generate a flight list with name and passport number to check identity on flight  

## Contents:

### Passenger

- How do we plan to make sure the data is persistent, when a passenger buys a ticket
we must be able to store their data

- We could use SQL to create our own database
- This database could contain tables that represent the info gathered from the user
- We should create a relational database
- The use of primary and foreign keys would allow us to retrieve info from different tables
- How much luggage are they able to take with them?

## Aeroplane

- How would we ensure the aeroplane has enough fuel to make a journey
- If for an unfortunate reason our plane crashed, how would we make sure we are still able to fly other passengers
- What is our plane model, what is it's capacity



## Database Connectivity
- create_connection file in which we will be able to create persistent data
- Being able to efficiently add and remove to the database on demand
- Being able to link the data stored in table through the usage of primary and foreign keys
