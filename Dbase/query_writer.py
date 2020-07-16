import pyodbc


server = "databases.spartaglobal.academy"  # Server name
database = "Airport_database_grp_3_v3"  # Database name
username = "SA"  # username
password = "Passw0rd2018"
connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + \
                                ";UID=" + username + ";PWD=" + password
connection_key = pyodbc.connect(connectionString, autocommit=True)
print("connected {}".format(database))

cursor = connection_key.cursor()
# print(cursor)
# cursor.execute('SELECT * FROM Assignments')
# row = cursor.fetchall()
# if row:
#     print(row)


var1 = "UPDATE Assignments SET PlaneID = 'AA115' WHERE Destination = 'Amsterdam'"
# var2 = " "



cursor.execute(var1)
cursor.commit()
# print(cursor.rowcount, 'Records Affected')


