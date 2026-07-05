from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def generate_pdf(file_path):
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()
    df = df.fillna(0)
    df["Total"] = df["Quantity"] * df["Price"]

    total_sales = df["Total"].sum()
    average_sales = df["Total"].mean()

    file_name = "reports/report.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Sales Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Total Sales: {total_sales}")
    c.drawString(50, 680, f"Average Sales: {average_sales}")

    y = 640
    c.drawString(50, y, "Product Details:")

    y -= 20

    for _, row in df.iterrows():
        c.drawString(50, y, f"{row['Product']} - {row['Category']} - {row['Total']}")
        y -= 20

    c.save()

    print("PDF Report Generated Successfully!")


if __name__ == "__main__":
    generate_pdf("data/sales.csv")