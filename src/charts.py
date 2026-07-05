import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load and prepare data
# -----------------------------
def load_data():
    df = pd.read_csv("data/sales.csv")
    df = df.dropna()
    df["Total"] = df["Quantity"] * df["Price"]
    return df


# -----------------------------
# BAR CHART
# -----------------------------
def bar_chart(df):
    sales = df.groupby("Category")["Total"].sum()

    plt.figure()
    sales.plot(kind="bar")

    plt.title("Category Wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.tight_layout()
    plt.savefig("reports/bar_chart.png")
    plt.close()


# -----------------------------
# LINE CHART
# -----------------------------
def line_chart(df):
    trend = df["Total"].cumsum()

    plt.figure()
    plt.plot(trend)

    plt.title("Sales Trend")
    plt.xlabel("Index")
    plt.ylabel("Cumulative Sales")

    plt.tight_layout()
    plt.savefig("reports/line_chart.png")
    plt.close()


# -----------------------------
# PIE CHART
# -----------------------------
def pie_chart(df):
    sales = df.groupby("Category")["Total"].sum()

    plt.figure()
    sales.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Sales Distribution")
    plt.ylabel("")

    plt.tight_layout()
    plt.savefig("reports/pie_chart.png")
    plt.close()


# -----------------------------
# SCATTER PLOT
# -----------------------------
def scatter_chart(df):
    plt.figure()
    plt.scatter(df["Quantity"], df["Price"])

    plt.title("Quantity vs Price")
    plt.xlabel("Quantity")
    plt.ylabel("Price")

    plt.tight_layout()
    plt.savefig("reports/scatter_chart.png")
    plt.close()


# -----------------------------
# RUN ALL CHARTS
# -----------------------------
def generate_charts():
    df = load_data()

    bar_chart(df)
    line_chart(df)
    pie_chart(df)
    scatter_chart(df)

    print("All charts generated successfully!")

if __name__ == "__main__":
    generate_charts()