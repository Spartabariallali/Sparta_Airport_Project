CREATE DATABASE Airport_database_grp_3;
DROP DATABASE Airport_database_grp_3
USE Airport_database_grp_3;
DROP TABLE Passengers

CREATE TABLE Passengers (
     PassengerID INTEGER NOT NULL IDENTITY(1,1)
    ,title VARCHAR(10)
    ,first_name VARCHAR(240)
    ,last_name VARCHAR(240)
    ,date_of_birth DATE
    -- ,gender VARCHAR(240)
    ,nationality VARCHAR(240)
    -- ,travel_documentation VARCHAR(240)
    ,travel_doc_number INT
    ,PRIMARY KEY (PassengerID)
    -- ,Foreign KEY(FlightID) REFERENCES Flights(FlightID)
    -- ,FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
)

CREATE TABLE Staff (
     StaffID INTEGER NOT NULL IDENTITY(1,1)
    ,first_name VARCHAR(240)
    ,last_name VARCHAR(240)
    ,job_role VARCHAR(240)
    ,username VARCHAR(50)
    ,[password] VARCHAR(100)
    ,PRIMARY KEY (StaffID)
)

CREATE TABLE Flights(
     FlightID INTEGER NOT NULL IDENTITY(1,1)
    ,flight_destination VARCHAR(240)
    ,flight_date VARCHAR(240)
    ,PRIMARY KEY (FlightID)
    ,AircraftID INT NOT NULL
    -- ,Foreign KEY(AircraftID) REFERENCES Aircraft(AircraftID)
    -- ,FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
)


CREATE TABLE Aircraft(
    AircraftID INTEGER NOT NULL IDENTITY(1,1)
    ,aircraft_type VARCHAR(240)
    PRIMARY KEY (AircraftID)
)

CREATE TABLE Bookings (
    BookingID INTEGER NOT NULL IDENTITY(1,1)
    ,booking_date DATE
    ,booking_total_fare FLOAT
    ,destination VARCHAR(240)
    ,flight_date VARCHAR(240)
    ,terminal VARCHAR(240)
    ,number_of_passengers INT
    ,PRIMARY KEY (BookingID)
)



SELECT * FROM Passengers


-- INSERT INTO [Passengers](title, first_name, last_name, gender, nationality,
--                          travel_documentation, travel_doc_number)
-- VALUES
