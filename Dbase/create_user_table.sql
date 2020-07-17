USE Airport_database_grp_3_v2
 
IF OBJECT_ID('Users', 'U') IS NOT NULL
DROP TABLE Users;

CREATE TABLE Users(
    StaffID INT IDENTITY(1,1)
    ,Username VARCHAR(30) NOT NULL
    ,UserPassword VARCHAR(192) NOT NULL
    ,PRIMARY KEY (StaffID)
);