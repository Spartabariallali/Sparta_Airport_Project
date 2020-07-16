import pyodbc
import pandas as pd

# server = 'databases.spartaglobal.academy'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'

class ConnectingToDataBase:
    
    def open_database(self):

        print("connecting to SQl server with ODBC driver")
        server = 'databases.spartaglobal.academy'
        database = 'Airport_database_grp_3_v3'
        username = 'SA'
        password = 'Passw0rd2018'
        connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        connection_key = pyodbc.connect(connection_string, autocommit=True)
        print("connected to the database")
        return connection_key


    def read_product_data(self):

        print("reading data")
        connection_string = obj.open_database()
        cursor = connection_string.cursor()
    # create a variable - query variable - use triple quotes
        cursor.execute("select productid, productname, supplierid, unitprice from products")
        rows = cursor.fetchall()
        # for row in rows:
        product_id = []
        product_name = []
        supplierid = []
        price = []
        for row in rows:
            product_id.append(row.productid)
            product_name.append(row.productname)
            supplierid.append(row.supplierid)
            price.append(row.unitprice)

        df = pd.DataFrame()

        df["product_id"] = product_id
        df["product_name"] = product_name
        df["supplierid"] = supplierid
        df["price"] = price

        print(df.head(len(product_id)))

    def create_product_data(self):

        print("creating data")
        connection_string = obj.open_database()
        cursor = connection_string.cursor()

        params = (product_name,price)
        cursor.execute("insert into product(name,price,created)) OUTPUT INSERTED.id values(?,?,getdate()); select SCOPE_IDENTITY()", params)
        row = cursor.fetchone()
        if row:
            print("Inserted Product ID is " + str(row[0]))
        
        connection_string.close()

        print("creating data")
        for index in range(1,5):
            product_name = 'product ' + str(index)
            price = 1.2 * index 
            create_product_data(product_name,price)
        print("done")

    def read_passenger_data(self):
        connection_string = obj.open_database()
        cursor = connection_string.cursor()
        query = ("SELECT * FROM Passengers")
        cursor.execute(query)
        rows = cursor.fetchall()







obj = ConnectingToDataBase()
obj.open_database()
obj.read_passenger_data()
# obj.read_product_data()

# obj.create_product_data