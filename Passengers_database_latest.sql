

CREATE DATABASE Airport_database_grp_3_v3;
DROP DATABASE Airport_database_grp_3_v3
USE Airport_database_grp_3_v3;


CREATE TABLE Staff (
     StaffID INTEGER NOT NULL IDENTITY(1,1)
    ,first_name VARCHAR(240)
    ,last_name VARCHAR(240)
    ,job_role VARCHAR(240)
    ,username VARCHAR(50)
    ,[password] VARCHAR(100)
    ,PRIMARY KEY (StaffID)
)

-- DROP TABLE Staff

CREATE TABLE Flights(
     FlightID INTEGER NOT NULL IDENTITY(1,1)
    ,flight_destination VARCHAR(240)
    ,PRIMARY KEY (FlightID)
)

-- DROP TABLE Flights
SELECT * FROM Flights

CREATE TABLE Bookings (
    BookingID INTEGER NOT NULL IDENTITY(1,1)
    ,booking_class VARCHAR (240)
    ,booking_way_trip VARCHAR(240)
    ,booking_destination VARCHAR(240)
    ,booking_price_per_passenger INT
    ,booking_no_of_passengers INT
    ,booking_total_fare FLOAT
    ,PRIMARY KEY (BookingID)
)

-- DROP TABLE Bookings
SELECT * FROM Bookings

SP_HELP Bookings

CREATE TABLE Passengers (
  PassengerID INTEGER NOT NULL IDENTITY(1,1),
  title varchar(10)NOT NULL,
  first_name varchar(50)NOT NULL,
  last_name varchar(50) NOT NULL,
  birthdate VARCHAR(240),
  nationality varchar(255)NOT NULL,
  travel_doc VARCHAR(240) NOT NULL,
  PRIMARY KEY (PassengerID)
)
DROP TABLE Passengers

INSERT INTO [Passengers](title, first_name, last_name, birthdate, nationality, travel_doc)
VALUES
('Ms.','Karli','Glover','1978-07-05','PT','123575774'),
('Dr.','Joanne','Rempel','2008-06-23','IE','22353576'),
('Mrs.','Rowena','Abbott','1977-09-14','MX','3536546'),
('Ms.','Electa','Morar','1973-12-16','CN','44532454'),
('Dr.','Ahmad','Haag','1973-02-02','IT','512353567'),
('Ms.','Jakayla','Zulauf','1996-07-16','GB','634652253'),
('Mrs.','Sydney','Lakin','2008-07-22','ES','72354223'),
('Dr.','Dayton','Bogan','1985-06-27','RU','83524124'),
('Mr.','Kristian','Bartoletti','1976-12-01','RU','95241324'),
('Ms.','Ebony','Ernser','1986-08-07','CA','1142214'),
('Miss','Damon','Frami','1978-11-17','FR','12412421'),
('Dr.','Marcella','Langworth','1982-01-08','CA','19421421'),
('Mrs.','Scotty','O''Kon','1979-06-17','RU','2021332'),
('Mrs.','Elvis','Smith','1977-07-30','GB','25321321'),
('Prof.','Dorthy','Legros','1993-09-16','RU','2832312'),
('Prof.','Noel','Rippin','2003-06-11','CN','29321321'),
('Mrs.','Noel','Ernser','1999-10-06','DE','32321321'),
('Dr.','Alphonso','Medhurst','1988-03-28','GB','4032123'),
('Mr.','Kaylie','Jaskolski','2006-05-29','FR','42321213'),
('Mr.','Sydnee','Marks','2012-02-22','IN','43321132'),
('Dr.','Torrance','Koss','1971-05-12','RU','482334234'),
('Ms.','Tabitha','Mraz','2002-06-24','PT','494235323'),
('Miss','Earnestine','Connelly','1996-12-27','ES','67423214'),
('Ms.','Josue','Murray','2014-02-18','PT','69342463'),
('Dr.','Ernestina','Renner','2014-04-21','IE','70325324'),
('Mrs.','Elinor','Hudson','1999-07-24','PT','72432346'),
('Prof.','Gwendolyn','Olson','1978-07-18','DE','75325432'),
('Mr.','Octavia','Jenkins','2006-12-09','CN','7632414'),
('Mrs.','Christian','Goldner','1992-03-13','ES','8242335'),
('Miss','Dayna','Pagac','1998-04-08','MX','8342352'),
('Dr.','Marlon','Bechtelar','1994-08-15','IN','84235221'),
('Prof.','Emiliano','Williamson','2011-08-21','IE','88'),
('Dr.','Gia','Swift','2013-07-23','GB','93'),
('Dr.','Dianna','Osinski','1978-11-15','DE','131'),
('Mrs.','Haven','Dicki','1974-04-08','IT','136'),
('Mr.','Moshe','Sporer','1975-06-10','IT','156'),
('Mr.','Randall','Nitzsche','1972-03-01','IE','160'),
('Dr.','Anita','Labadie','1990-01-13','IN','168'),
('Mr.','Cassandre','Breitenberg','2017-06-10','US','176'),
('Miss','Hilton','Hilll','1998-02-27','IN','177'),
('Prof.','Ida','Schmitt','2005-01-20','FR','216'),
('Prof.','Ida','Gorczany','2019-06-25','US','228'),
('Miss','Idell','Gerhold','1985-07-03','ES','235'),
('Prof.','Dan','Fahey','1985-05-10','PT','268'),
('Miss','Maybelle','Wehner','1972-06-27','MX','296'),
('Miss','Wanda','Kunze','1998-01-02','IN','309'),
('Dr.','Anthony','Hettinger','1976-01-24','IT','317'),
('Miss','Domingo','Schaden','2005-12-26','US','412'),
('Prof.','Garrison','Fadel','2017-03-27','FR','448'),
('Dr.','Mayra','Gusikowski','2009-11-17','CN','491'),
('Ms.','Libby','Beer','2002-01-14','IE','535'),
('Prof.','Jewel','Larkin','2006-06-27','FR','538432'),
('Ms.','Mavis','Wisozk','2009-05-05','IE','624243'),
('Mr.','Hortense','Huels','1971-08-05','MX','664'),
('Dr.','Eliza','Larson','2008-03-16','GB','688'),
('Dr.','Zula','Rutherford','1980-08-07','ES','696'),
('Dr.','Lucious','Crooks','2015-06-23','US','773'),
('Dr.','Roslyn','Yost','1990-07-12','ES','832'),
('Prof.','Marta','Wunsch','1974-07-30','IE','851'),
('Miss','Fiona','Walker','1974-01-26','GB','865'),
('Miss','Derrick','Flatley','2013-05-14','ES','895'),
('Ms.','Michelle','Sanford','2008-03-03','FR','910'),
('Prof.','Jesus','Wyman','1980-02-21','CN','968'),
('Prof.','Helmer','Weissnat','2009-08-26','MX','1297'),
('Ms.','Shaylee','Mills','1971-05-22','DE','1427'),
('Prof.','Norma','Paucek','1998-12-13','IN','1461'),
('Dr.','Eduardo','Reilly','1986-04-26','CN','1647'),
('Prof.','Kadin','Zemlak','2014-10-25','CN','2095'),
('Mrs.','Daryl','Blick','1999-04-11','RU','2773'),
('Ms.','Garrison','Fisher','2000-10-29','IT','3048'),
('Dr.','Darrell','Nicolas','2000-04-24','IT','3139'),
('Prof.','Ofelia','Ruecker','1977-10-19','GB','3152'),
('Prof.','Jason','Zieme','1973-04-30','FR','3276'),
('Prof.','Jude','Mitchell','2005-02-21','CN','3295'),
('Dr.','Abby','Daugherty','2013-05-14','FR','4209'),
('Prof.','Alaina','Johnston','1996-04-29','ES','4635'),
('Mr.','Skylar','Becker','2017-10-03','DE','4657'),
('Mr.','Milford','O''Reilly','2011-03-01','DE','4858'),
('Ms.','Karli','Heaney','1973-06-12','MX','5390342'),
('Prof.','Bart','Muller','1989-04-10','ES','54663342'),
('Prof.','Wilhelmine','Abernathy','1984-12-16','FR','5782432'),
('Dr.','Amparo','Dach','1971-01-22','CA','5864320'),
('Dr.','Elna','Eichmann','2009-12-16','FR','5877'),
('Prof.','Newton','Harris','1996-04-26','US','6507'),
('Dr.','Emilio','Frami','2014-10-27','PT','6650'),
('Prof.','Akeem','Rodriguez','2010-01-26','CN','7469'),
('Prof.','Gavin','Bahringer','1977-11-18','US','7554'),
('Mr.','Cesar','Kuvalis','2006-04-11','IE','7569'),
('Dr.','Jaida','O''Reilly','1973-11-27','US','7730'),
('Ms.','Christop','Kling','2017-02-03','IE','8300'),
('Mr.','Kyle','Steuber','1986-04-13','ES','8397'),
('Prof.','Darron','Schmeler','2014-08-27','IN','8420'),
('Prof.','Maude','Hodkiewicz','2015-02-23','FR','8503'),
('Ms.','Abbie','Keeling','2011-08-28','MX','8751'),
('Dr.','Jamarcus','Thompson','2014-06-01','IE','8897'),
('Miss','Miles','Boyle','1986-08-28','CA','9056'),
('Dr.','Timmothy','Abbott','2005-02-08','US','9125'),
('Prof.','Abdul','Mraz','2010-03-21','PT','9157'),
('Mr.','Ardella','Sporer','2014-04-03','DE','9169'),
('Ms.','Kaley','Considine','1997-08-25','MX','9738'),
('Prof.','Pat','Yundt','2007-02-02','IE','11419'),
('Mr.','Robin','Lemke','1985-06-06','DE','12905'),
('Dr.','Clotilde','Gislason','1995-03-17','IE','14615'),
('Mrs.','Yadira','Abshire','2008-06-27','IE','15224'),
('Dr.','Tanya','Bergnaum','2012-07-06','US','18839'),
('Miss','Percival','Runolfsson','1995-01-24','RU','19706'),
('Dr.','Aglae','Gorczany','1977-12-21','DE','20924'),
('Dr.','Darrick','Wolff','2001-10-11','GB','22022'),
('Mr.','Alisha','Lesch','1977-11-06','IE','26424'),
('Mr.','Nia','Carter','2003-04-22','DE','35075'),
('Miss','Curt','Leuschke','1996-12-02','IE','36177'),
('Prof.','Jerad','Bradtke','2013-01-21','GB','37567'),
('Dr.','Merlin','Hammes','2003-03-16','US','38324'),
('Mr.','Wilber','Feeney','2019-07-24','FR','41429'),
('Prof.','Keara','Wilkinson','1991-06-06','IN','43241'),
('Prof.','Keyshawn','Denesik','1983-03-06','IT','53458'),
('Prof.','Jerrod','Welch','1989-04-18','IT','53855'),
('Miss','Carleton','Koelpin','2019-01-29','PT','58942'),
('Ms.','Kristian','Herzog','1974-04-10','FR','61081'),
('Dr.','Otha','Upton','2008-05-03','ES','62707'),
('Dr.','Marlee','Connelly','1988-06-12','US','64190'),
('Ms.','Guillermo','Dach','1998-04-18','IT','67069'),
('Mr.','Dorcas','Kassulke','2010-09-30','IE','71798'),
('Dr.','Naomi','Kovacek','1994-08-08','GB','72162'),
('Mr.','Porter','Crona','1991-02-16','MX','74907'),
('Mrs.','Lelah','Wyman','2010-09-08','RU','75517'),
('Ms.','Jarod','Trantow','1988-10-31','DE','79948'),
('Prof.','Ole','Rosenbaum','2003-06-08','ES','83789'),
('Mr.','Brandon','Nolan','1996-11-22','IT','85632'),
('Prof.','Burnice','Willms','1998-07-16','PT','86069'),
('Miss','Maegan','Mayer','2008-10-18','RU','90186'),
('Mr.','Royal','Ratke','1972-09-15','GB','90768'),
('Prof.','Charlie','Collier','1984-07-07','MX','92565'),
('Dr.','Vita','Barrows','2012-12-07','GB','92589'),
('Ms.','Ottilie','Herzog','1997-04-12','MX','94165'),
('Ms.','Ezra','Mitchell','1991-06-06','IN','95653'),
('Dr.','Eleazar','Reinger','1985-04-09','IN','99122'),
('Miss','Chadrick','McKenzie','1997-06-08','IN','197843'),
('Prof.','Domingo','Batz','2010-01-31','CA','210530'),
('Dr.','Antonio','Johns','2008-04-21','PT','211013'),
('Ms.','Jada','Cremin','2004-03-08','DE','238912'),
('Dr.','Lambert','Moen','2014-01-28','PT','270143'),
('Ms.','Katelin','Conn','1993-06-09','GB','276681'),
('Prof.','Kurt','Skiles','1992-09-24','PT','277478'),
('Dr.','Jefferey','Gaylord','2007-02-08','ES','296495'),
('Ms.','Abbie','Bashirian','1974-08-03','CN','297277'),
('Prof.','Ocie','White','2017-08-15','CN','302387'),
('Mrs.','Birdie','Kertzmann','1981-06-12','MX','312289'),
('Dr.','Cicero','Hauck','1991-12-05','CA','316502'),
('Miss','Melba','Koelpin','1991-08-24','MX','324026'),
('Dr.','Lolita','Barton','1975-01-10','CA','332173'),
('Miss','Mariela','Herman','1993-12-16','US','363384'),
('Mrs.','Hayley','Mohr','2001-09-03','GB','368855'),
('Prof.','Kyra','Rolfson','2004-06-04','DE','381511'),
('Miss','Raquel','Murphy','1986-06-17','GB','383403'),
('Dr.','Abdul','Gorczany','2007-07-27','MX','403524'),
('Prof.','Marlee','Bailey','1989-08-13','IT','405546'),
('Dr.','Kiel','Runte','2009-11-24','PT','428311'),
('Miss','Yoshiko','Homenick','1988-07-24','PT','444568'),
('Dr.','Esmeralda','Rogahn','2010-10-07','US','444647'),
('Ms.','Sid','Volkman','2015-01-30','IT','467945'),
('Prof.','Lou','Fisher','1975-02-02','IE','549711'),
('Mrs.','Garnet','Tremblay','2000-11-06','IE','557705'),
('Miss','Amelie','Deckow','1972-04-10','MX','558253'),
('Mr.','Rollin','Christiansen','1990-03-21','RU','560740'),
('Dr.','Louvenia','Koepp','2015-08-22','IN','590837'),
('Prof.','Gwendolyn','Kunde','1991-04-13','PT','675938'),
('Prof.','Bella','Swift','2000-02-03','RU','680150'),
('Dr.','Peggie','Bins','1997-12-21','DE','698477'),
('Miss','Ricky','Schoen','2000-07-04','ES','769274'),
('Dr.','Esteban','Harris','1998-09-14','PT','775835'),
('Miss','Doyle','Fisher','1980-11-04','MX','783381'),
('Miss','Duncan','Mitchell','1970-01-24','CA','787899'),
('Mrs.','Stevie','Hills','2000-12-18','GB','847726'),
('Mr.','Ronaldo','Marquardt','1998-09-24','IN','884456'),
('Dr.','Keeley','Wolff','1979-08-28','MX','895677'),
('Dr.','Lucious','Marquardt','1993-06-13','DE','1023674'),
('Prof.','Destini','Donnelly','1998-11-24','MX','1362605'),
('Miss','Jerrell','Wolf','2017-07-22','CA','1407424'),
('Miss','Leanna','Crist','2019-03-21','ES','1577171'),
('Miss','Rubie','Kohler','1988-06-18','CN','2326747'),
('Prof.','Liana','Hackett','1999-02-25','MX','2486556'),
('Prof.','Kirsten','Waters','1998-07-20','IT','2589879'),
('Dr.','Kaleb','Lueilwitz','1970-11-02','US','2787502'),
('Dr.','Rudy','Mosciski','1983-01-03','CA','3419976'),
('Miss','Cleveland','Cummerata','1979-09-23','US','4008485'),
('Prof.','Brendan','Luettgen','1985-05-17','FR','4279176'),
('Dr.','Anastacio','Bahringer','1986-01-02','PT','4527249'),
('Prof.','Rudy','Eichmann','1991-06-16','US','4678417'),
('Mr.','Caleb','Russel','2015-07-26','IN','4752969'),
('Ms.','Sheridan','Homenick','2019-08-22','US','5017844'),
('Mr.','Ryan','Crooks','1992-05-05','CN','5584101'),
('Prof.','Julien','Hermann','1980-04-25','CA','5612995'),
('Mr.','Jannie','Ratke','2000-04-20','GB','5827140'),
('Prof.','Della','Hegmann','1995-04-16','IE','5896066'),
('Prof.','Emiliano','Gottlieb','2017-03-16','RU','6404408'),
('Prof.','Burley','Zboncak','1979-06-12','RU','6719423'),
('Miss','Maurice','Bayer','2002-02-12','IN','6788047'),
('Prof.','Derrick','Homenick','1996-05-02','IN','7068438'),
('Mrs.','Giovani','Prosacco','1978-10-31','FR','7200479'),
('Prof.','Arvel','Johnson','2018-07-29','CN','7419847'),
('Ms.','Jerald','Schowalter','1972-12-16','MX','7437252'),
('Miss','Rodger','Monahan','1984-06-13','FR','8477626'),
('Mrs.','Isac','Stracke','1975-04-09','CN','9060938'),
('Dr.','Rosanna','Donnelly','1980-06-02','US','9419087'),
('Ms.','Margie','Rippin','1989-05-25','CA','9463484'),
('Mrs.','Kelsie','Mills','1982-12-23','DE','9546306'),
('Prof.','Albert','Swaniawski','2018-11-10','US','9892576'),
('Mr.','Jaime','Boyle','1985-09-21','PT','9996790'),
('Dr.','Elisa','Bernier','2002-10-04','ES','16088803'),
('Ms.','Clifford','Ernser','1990-07-28','MX','17666176'),
('Mrs.','Kristofer','Stanton','1970-05-31','IN','17825895'),
('Dr.','Maymie','Schmeler','2018-06-09','CA','18601275'),
('Prof.','Retha','Howell','1975-09-14','FR','19095053'),
('Prof.','Charley','Donnelly','1994-09-03','CN','19729062'),
('Prof.','Jeanette','Koelpin','2004-10-26','IT','22487463'),
('Ms.','Jeff','Dickens','1986-02-08','IT','24134033'),
('Dr.','Bart','Sawayn','1999-07-11','RU','25868489'),
('Prof.','Kacey','Olson','1970-05-28','GB','28480195'),
('Ms.','Grover','Hegmann','2017-10-19','IT','30915171'),
('Miss','Florence','Kemmer','1989-12-13','IN','31660403'),
('Prof.','Lavern','Wyman','1990-10-12','IN','34525321'),
('Ms.','Alysa','Okuneva','1994-12-24','FR','35518734'),
('Prof.','Tre','Runolfsdottir','1979-08-05','IT','36429891'),
('Prof.','Andreanne','Ryan','1991-03-19','FR','38583294'),
('Mr.','Paolo','Greenfelder','1973-05-26','PT','47629695'),
('Dr.','Emmy','Purdy','1991-05-21','RU','49753569'),
('Ms.','Lonny','Nolan','1991-03-25','PT','50012366'),
('Dr.','Merl','Beahan','1978-07-27','US','55055287'),
('Prof.','Terrence','Haag','1983-10-05','RU','55511737'),
('Dr.','Adam','Kshlerin','2013-03-30','DE','55833664'),
('Ms.','Americo','O''Kon','1990-03-09','RU','57188202'),
('Miss','Emmitt','Ullrich','1987-11-30','IE','59404295'),
('Dr.','Floy','Pacocha','1976-12-07','DE','59432288'),
('Mr.','Morton','Pagac','1992-09-11','US','64769129'),
('Prof.','Fanny','Mitchell','1991-04-05','FR','65726614'),
('Dr.','Jermain','Kreiger','2007-09-26','MX','66976710'),
('Prof.','Mable','Legros','2001-02-28','CN','68299119'),
('Ms.','Frank','Gleichner','1976-02-09','CN','68414014'),
('Mr.','Mackenzie','Strosin','1976-03-11','US','68424512'),
('Mrs.','Joe','Hilpert','1976-10-22','US','68774956'),
('Dr.','Jacey','Cummerata','2006-04-25','GB','69703803'),
('Prof.','Angelita','Torp','1984-12-20','IN','70801470'),
('Dr.','Leonel','Schroeder','2009-09-07','DE','74764396'),
('Prof.','Elmore','Franecki','1988-03-03','CN','78420978'),
('Prof.','Buster','O''Connell','1984-07-09','IT','84953245'),
('Miss','Carley','Botsford','2020-07-15','GB','85847197'),
('Prof.','Kathryne','Haag','1990-12-30','GB','87991326'),
('Mrs.','Katarina','Breitenberg','1988-01-14','IN','92028443'),
('Dr.','Willis','Dooley','1975-01-21','FR','92278970'),
('Mrs.','Abby','Connelly','1972-03-25','FR','93664039'),
('Miss','Verna','Dibbert','1997-07-13','IN','93976861'),
('Prof.','Christian','Rutherford','1999-07-14','IN','94752121'),
('Prof.','Gillian','Sipes','1985-02-06','IE','133108150'),
('Ms.','Brycen','Gorczany','2009-01-31','IN','144041179'),
('Ms.','Arianna','Koelpin','2019-05-14','PT','169216231'),
('Dr.','Trycia','DuBuque','1970-11-05','RU','193644141'),
('Ms.','Enrico','Jones','2015-01-19','IE','198621257'),
('Mr.','Karlie','Bogan','1985-03-09','MX','227794074'),
('Prof.','Lawson','Stroman','1994-10-14','MX','238505522'),
('Prof.','Baron','Green','1971-12-31','PT','257229221'),
('Mr.','Hyman','Pouros','1988-05-24','MX','275341569'),
('Dr.','Patricia','Mueller','2011-01-11','CA','277159208'),
('Prof.','Jovan','Cronin','1976-01-23','US','287996845'),
('Dr.','Theresa','Miller','1973-01-06','CN','327586700'),
('Ms.','Gilda','Schowalter','1970-02-26','DE','360813130'),
('Ms.','Ike','Zulauf','1982-10-05','GB','373450865'),
('Prof.','Juliana','Strosin','2017-02-10','CA','407384114'),
('Dr.','Jermaine','Morissette','1974-08-29','US','417647743'),
('Prof.','Cleo','Zulauf','1997-10-28','IT','480300104'),
('Mr.','Jo','Padberg','2008-06-23','GB','487336925'),
('Ms.','Angela','Rippin','1980-06-09','FR','539329625'),
('Prof.','Jerad','Beahan','1973-05-13','GB','539429828'),
('Dr.','Delaney','Skiles','2002-01-12','IE','566529106'),
('Prof.','Darrell','Hansen','1994-12-21','IE','576421805'),
('Dr.','Amiya','Mitchell','1980-02-27','CN','618867658'),
('Dr.','Nayeli','Maggio','1974-06-04','PT','684266275'),
('Prof.','Odessa','Willms','2010-07-04','IT','685416237'),
('Ms.','Ashly','Johns','1991-07-10','RU','690772637'),
('Dr.','Cecil','Romaguera','1980-12-17','RU','691705928'),
('Prof.','Benny','Jakubowski','1998-12-22','IN','727614949'),
('Miss','Karli','Luettgen','1976-04-08','US','749326703'),
('Mrs.','Desiree','Veum','2005-01-01','US','750558638'),
('Dr.','Demario','Bashirian','2020-07-10','ES','756937056'),
('Dr.','Emmanuelle','Boyer','2014-11-28','RU','757212503'),
('Dr.','Lucy','Gleichner','1993-12-14','GB','764635933'),
('Prof.','Madisen','Nitzsche','2004-07-30','PT','776084541'),
('Dr.','Tomasa','Lynch','1993-05-22','GB','780413590'),
('Mr.','Sage','Kemmer','2002-07-28','CA','880884713'),
('Mr.','Chad','Kreiger','1979-07-06','GB','894258418'),
('Mrs.','Lesley','Flatley','1976-02-26','IT','916034795'),
('Dr.','Hal','Carroll','1977-08-20','IT','918142662'),
('Prof.','Bethel','Brakus','1984-01-08','IE','927266114'),
('Prof.','Maurice','Dickinson','1987-08-30','CN','933141194'),
('Dr.','Rowena','Bogisich','1989-07-20','ES','934725651'),
('Ms.','Sibyl','Dicki','1993-07-25','IN','936481555'),
('Dr.','Ludie','Rosenbaum','1993-01-14','IN','979910293'),
('Mr.','Leland','Langworth','1980-03-30','MX','983824465'),
('Miss','Magnolia','Haley','2004-03-27','RU','990581644'), 
('Mrs.','Rafael','Roberts','2013-12-13','MX','81981000'),
('Prof.','Naomie','O''Hara','2011-04-19','DE','4800'),
('Prof.','Madisen','Beer','2015-10-20','CA','86'),
('Prof.','Jazmyne','Daniel','2020-01-14','CN','93001908'),
('Prof.','Bulah','Pfannerstill','2018-07-07','GB','4546323'),
('Mr.','Henry','Donnelly','1993-12-27','MX','7539710'),
('Dr.','Clotilde','Rippin','1990-12-30','FR','338'),
('Mrs.','Chelsea','Walker','2007-11-08','DE','45425675215'),
('Mr.','Jena','Kertzmann','1992-11-29','FR','3457863225'),
('Prof.','Brice','Schultz','1972-08-02','RU','2213625'),
('Dr.','Travis','Torphy','1971-10-25','US','6225'),
('Mrs.','Imogene','Kuhic','2014-12-21','FR','47'),
('Ms.','Faye','Kub','1977-05-31','PT','753'),
('Mr.','Sincere','Koepp','2008-08-17','RU','77766299'),
('Prof.','Evan','Bauch','1973-02-17','US','470'),
('Dr.','Izabella','Langosh','1997-05-18','DE','6456959'),
('Mrs.','Aurelie','VonRueden','1987-06-30','FR','97'),
('Mr.','Roderick','Nolan','2001-03-20','IN','182906'),
('Mrs.','Reese','Ruecker','2006-01-19','MX','20'),
('Ms.','Abelardo','Mitchell','1982-03-05','CA','288514'),
('Dr.','Christian','Kuhn','1985-07-20','IE','19697'),
('Prof.','Donny','Reinger','2002-06-02','CA','63'),
('Prof.','Shaniya','Becker','2014-11-29','US','752'),
('Mr.','Damaris','Konopelski','2012-01-28','CN','853517'),
('Miss','Gordon','Schaefer','1997-07-01','IT','39684729453'),
('Prof.','Lilyan','Steuber','1997-04-16','CN','65'),
('Dr.','Enrique','Zboncak','2012-12-10','DE','4021276'),
('Mr.','Bonnie','Christiansen','2012-12-10','CN','208309'),
('Miss','Iva','Borer','1983-01-05','IT','4206'),
('Miss','Ryley','Kub','1980-08-26','PT','573'),
('Prof.','Jaeden','Funk','2006-07-14','GB','534120'),
('Mr.','Bridie','Halvorson','2009-03-04','MX','9499')

SELECT * FROM Passengers



