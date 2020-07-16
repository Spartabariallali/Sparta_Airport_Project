from database.create_connection import Database_OOP
import numpy as np
import pandas as pd
import time



class Check_all_passengers:
    def all_passsengers(self):
        obj1 = Database_OOP()
        cursor = obj1.establish_connection()
        query = """SELECT * FROM Passengers"""
        rows = cursor.execute(query)
        for row in rows:
            print(row)
        # title = []
        # first_name = []
        # last_name = []
        # birthdate = []
        # nationality = []
        # travel_doc = []
        # for row in rows:
        #     title.append(row.title)
        #     first_name.append(first_name)
        #     last_name.append(last_name)
        #     birthdate.append(birthdate)
        #     nationality.append(nationality)
        #     travel_doc.append(travel_doc)
        # df = pd.DataFrame()
        # df["title"] = title
        # df["first_name"] = first_name
        # df["last_name"] = last_name
        # df["birthdate"] = birthdate
        # df["nationality"] = nationality
        # df["travel_doc"] = travel_doc
        # pd.set_option("display.max_rows", len(title))
        #
        # print(df.head(len(title)))

        print("Returning back to the Main Menu...")
        time.sleep(3)
        return
