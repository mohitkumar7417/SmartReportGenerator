import pandas as pd

file_path = "data/sales.xlsx"

df = pd.read_excel(file_path, engine="openpyxl")

print("Excel Loaded Successfully\n")
print(df)