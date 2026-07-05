from report_generator import generate_report
from pdf_generator import generate_pdf

def run_all_reports():
    file_path = "data/sales.csv"

    print("Generating HTML Report...")
    generate_report(file_path)

    print("\nGenerating PDF Report...")
    generate_pdf(file_path)

    print("\nAll Reports Generated Successfully!")


if __name__ == "__main__":
    run_all_reports()