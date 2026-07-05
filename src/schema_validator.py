import pandas as pd

def validate_schema(df):
    required_columns = ["Product", "Category", "Quantity", "Price"]

    for col in required_columns:
        if col not in df.columns:
            print(f"Missing column: {col}")
            return False

    print("Schema Validation Passed")
    return True