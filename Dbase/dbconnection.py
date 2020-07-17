import pyodbc
import pandas as pd
import pandas.io.sql
# i have stored the credentials in a separate file which will be ignored to keep them private

# I put my credentials here below my class because it becomes available to everything in the class
class OpenConnection:
#     # Database Login credentials
    def connections(self):
        server = "databases.spartaglobal.academy"  # Server name
        database = "Airport_database_grp_3_v2"  # Database name
        username = "SA"  # username
        password = "Passw0rd2018"
        connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + \
                                        ";UID=" + username + ";PWD=" + password
        connection_key = pyodbc.connect(connectionString, autocommit=True)
        print("connected {}".format(database))
        df = pandas.io.sql.read_sql('SELECT * FROM Aircraft', connection_key)
        pd.set_option('display.max_rows', None, 'display.max_columns', None)
        print(df)
