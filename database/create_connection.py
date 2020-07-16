import pyodbc
import SecretWeapons.secret_file


class Database_OOP:
    server = SecretWeapons.secret_file.server
    database = SecretWeapons.secret_file.database
    username = SecretWeapons.secret_file.username
    password = SecretWeapons.secret_file.password

    # this method is specifically for establishing a connection
    def establish_connection(self):
        connections = ('DRIVER={ODBC Driver 17 for SQL Server};'
                                     'SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection Successful")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("Connection Timed Out, retrying...")
            self.establish_connection()
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface, retrying...")
            self.establish_connection()
        else:
            cursor = connection.cursor()
            return cursor
