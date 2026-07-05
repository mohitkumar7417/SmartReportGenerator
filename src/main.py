import typer

from analysis import run_analysis
from charts import generate_charts
from report_generator import generate_report
from pdf_generator import generate_pdf

app = typer.Typer()


@app.command()
def analysis():
    """Run statistical analysis."""
    run_analysis("data/sales.csv")


@app.command()
def charts():
    """Generate charts."""
    generate_charts()


@app.command("html-report")
def html_report():
    """Generate HTML report."""
    generate_report("data/sales.csv")


@app.command("pdf-report")
def pdf_report():
    """Generate PDF report."""
    generate_pdf("data/sales.csv")


if __name__ == "__main__":
    app()