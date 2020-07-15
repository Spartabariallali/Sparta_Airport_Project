import pyodbc
import secret_file


class Database_OOP:
    server = secret_file.server
    database = secret_file.database
    username = secret_file.username
    password = secret_file.password

    # this method is specifically for establishing a connection
    def establish_connection(self):
        connections = ('DRIVER={ODBC Driver 17 for SQL Server};'
                                     'SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection Successful")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("Connection Timed Out")
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface")
        else:
            cursor = connection.cursor()
            return cursor


# obj = Database_OOP()
# obj.establish_connection()