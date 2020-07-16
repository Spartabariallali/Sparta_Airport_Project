# Shared Repository for those in Group 3 working on the airlines Project

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
 

## Passenger

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

## User Stories
- I want to be able to create a passenger list with name and passport number, so that I can add them to flight
- As an airport assistant I want to be able to create flight trip with specific destination
- I want to be able to assign and or change my plane to my flight trip, input my password so I can handle the problem
- I want to be able to add passengers to flight trip so I can sell tickets to them
- I want to be able to generate a flight attendees list report that lists of passengers name and passports, so that I can check their identity document


## Database Connectivity
- create_connection file in which we will be able to create persistant data
- Being able to efficiently add and remove to the database on demand
- Being able to link the data stored in table through the usage of primary and foreign keys
-
-

### Logical Ordering of Events

- We want to be able to first ask them where they want to travel to
- Then we will ask them for their personal details
- Then we will create a booking card and booking id for them