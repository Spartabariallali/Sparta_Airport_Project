import pyodbc
# i have stored the credentials in a separate file which will be ignored to keep them private
import classified_port
# I put my credentials here below my class because it becomes available to everything in the class
class OpenConnection:
    # Database Login credentials
    server = classified_port.server
    database = classified_port.database
    username = classified_port.username
    password = classified_port.password

    def credentials(self):
        connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + \
                           ";UID=" + self.username + ";PWD=" + self.password
        try:
            with pyodbc.connect(connectionString, timeout=5) as connection:
                print("Connection established")
        except:
            print("Connection Timed out")
        else:
            cursor = connection.cursor()
            return cursor
obj = OpenConnection()
        # this serves as a link between my credentials method and my queries method. Without it, i would have no access to my cursor variable
cursor = obj.credentials()


obj.username_check('SELECT * FROM Users')