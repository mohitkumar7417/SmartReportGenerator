import pandas as pd
import json
import sqlite3


class DataSource:

    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        print("\nCSV Data:\n")
        print(df)
        return df

    def read_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        print("\nJSON Data:\n")
        print(data)
        return data

    def read_sqlite(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()

        print("\nSQLite Data:\n")
        for row in rows:
            print(row)

        conn.close()
        return rows


if __name__ == "__main__":
    ds = DataSource()

    ds.read_csv("data/sales.csv")
    ds.read_json("data/sales.json")
    ds.read_sqlite("sales.db")