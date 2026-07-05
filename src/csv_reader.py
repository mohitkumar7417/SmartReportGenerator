import pandas as pd
from schema_validator import validate_schema

file_path = "data/sales.csv"

df = pd.read_csv(file_path)

print("CSV Loaded Successfully\n")
print(df)

validate_schema(df)