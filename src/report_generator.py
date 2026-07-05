import pandas as pd
from jinja2 import Environment, FileSystemLoader


def generate_report(file_path):
    # Read CSV
    df = pd.read_csv(file_path)

    # Data processing
    df = df.drop_duplicates()
    df = df.fillna(0)
    df["Total"] = df["Quantity"] * df["Price"]

    # Statistics
    total_sales = df["Total"].sum()
    average_sales = df["Total"].mean()
    category_sales = df.groupby("Category")["Total"].sum()

    # Jinja2 setup
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    # Render HTML
    html_output = template.render(
        total_sales=total_sales,
        average_sales=average_sales,
        category_sales=category_sales.to_dict(),
        table=df.to_html(index=False),
        chart="bar_chart.png"
    )

    # Save HTML file
    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("HTML Report Generated Successfully!")


if __name__ == "__main__":
    generate_report("data/sales.csv")