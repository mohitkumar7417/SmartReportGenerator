import pandas as pd


def run_analysis(file_path):
    df = pd.read_csv(file_path)

    # Clean
    df = df.drop_duplicates()
    df = df.fillna(0)

    # Transform
    df["Total"] = df["Quantity"] * df["Price"]

    # Statistical Analysis
    total = df["Total"].sum()
    avg = df["Total"].mean()
    median = df["Total"].median()
    std_dev = df["Total"].std()

    # Percentiles
    p25 = df["Total"].quantile(0.25)
    p50 = df["Total"].quantile(0.50)
    p75 = df["Total"].quantile(0.75)

    # Group-by Aggregation
    category_sales = df.groupby("Category")["Total"].sum()

    print("\n====== ANALYSIS REPORT ======\n")

    print(df)

    print("\nTotal Sales:", total)
    print("Average Sales:", avg)
    print("Median Sales:", median)
    print("Standard Deviation:", std_dev)

    print("\nPercentiles")
    print("25th Percentile:", p25)
    print("50th Percentile:", p50)
    print("75th Percentile:", p75)

    print("\nCategory Wise Sales:\n")
    print(category_sales)


if __name__ == "__main__":
    run_analysis("data/sales.csv")