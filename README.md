# AutoReport

## Overview
AutoReport is a Python-based automated reporting and analytics tool. It reads sales data, performs statistical analysis, generates charts, creates an HTML report, and exports a PDF report.

## Features
- CSV and Excel data reading
- JSON and SQLite support
- Data cleaning
- Statistical analysis
  - Total
  - Average
  - Median
  - Standard Deviation
  - Percentiles
  - Category-wise aggregation
- Chart generation
  - Bar Chart
  - Line Chart
  - Pie Chart
  - Scatter Plot
- HTML report generation
- PDF report generation
- Command Line Interface (Typer)
- Automated testing with Pytest

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jinja2
- ReportLab
- Typer
- Pytest

## Project Structure

```
AutoReport/
├── data/
├── reports/
├── src/
├── templates/
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation

```
pip install -r requirements.txt
```

## Run

```
python src/main.py analysis
python src/main.py charts
python src/main.py html-report
python src/main.py pdf-report
```

## Testing


pytest


## Author

Mohit Kumar