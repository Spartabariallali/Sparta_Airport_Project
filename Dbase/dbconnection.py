import pyodbc
import pandas as pd
import pandas.io.sql
# i have stored the credentials in a separate file which will be ignored to keep them private
import classified_port
# I put my credentials here below my class because it becomes available to everything in the class
class OpenConnection:
#     # Database Login credentials
    def connections(self):
        server = "databases.spartaglobal.academy"  # Server name
        database = "Airport_database_grp_3_v3"  # Database name
        username = "SA"  # username
        password = "Passw0rd2018"
        connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + \
                                        ";UID=" + username + ";PWD=" + password
        connection_key = pyodbc.connect(connectionString, autocommit=True)
        print("connected {}".format(database))
        df = pandas.io.sql.read_sql('SELECT * FROM Assignments', connection_key)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)
        print(df)
# con = OpenConnection()
# con.connections()





#     def credentials(self):
#         connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + \
#                            ";UID=" + self.username + ";PWD=" + self.password
#         try:
#             with pyodbc.connect(connectionString, timeout=5) as connection:
#                 print("Connection established")
#         except:
#             print("Connection Timed out")
#         else:
#             cursor = connection.cursor()
#             return cursor
# obj = OpenConnection()
#         # this serves as a link between my credentials method and my queries method. Without it, i would have no access to my cursor variable
# cursor = obj.credentials()
#
# query = cursor.execute("SELECT * FROM Assignments")
# rows = query.fetchone()
# print(rows)