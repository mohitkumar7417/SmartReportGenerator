import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pandas as pd
from analysis import run_analysis


def test_run_analysis(capsys):
    data = {
        "Product": ["Laptop", "Mouse"],
        "Category": ["Electronics", "Electronics"],
        "Quantity": [2, 5],
        "Price": [50000, 500]
    }

    df = pd.DataFrame(data)

    os.makedirs("data", exist_ok=True)
    test_file = "data/test_sales.csv"
    df.to_csv(test_file, index=False)

    run_analysis(test_file)

    captured = capsys.readouterr()

    assert "ANALYSIS REPORT" in captured.out
    assert "Total Sales:" in captured.out
    assert "Average Sales:" in captured.out
    assert "Median Sales:" in captured.out
    assert "Standard Deviation:" in captured.out
    assert "Category Wise Sales:" in captured.out