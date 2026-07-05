import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    print("\nOriginal Data:\n")
    print(df)

    # Clean data
    df = df.drop_duplicates()
    df = df.fillna(0)

    # Transformation
    df["Total"] = df["Quantity"] * df["Price"]

    print("\nProcessed Data:\n")
    print(df)

    # Statistics
    print("\nStatistics:\n")
    print("Total Sales Sum:", df["Total"].sum())
    print("Average Sales:", df["Total"].mean())

    # Group-by analysis
    print("\nCategory-wise Sales:\n")
    category_sales = df.groupby("Category")["Total"].sum()
    print(category_sales)


if __name__ == "__main__":
    analyze_data("data/sales.csv")