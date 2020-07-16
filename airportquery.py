from dbconnection import ConnectingToDataBase
import pandas as pd

class QueryingData:

    def read_product_data(self):

        print("reading data")
        connection_string = obj2.open_database()
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




obj2= QueryingData()
obj2.read_product_data()