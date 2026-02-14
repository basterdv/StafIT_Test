from src.parser import parse_csv_files
from src.reports import AverageReport


def test_parse_csv_files(sample_csv_file):
    data = parse_csv_files(sample_csv_file)
    assert len(data) == 18
    assert data[0]["country"] == "United States"
    assert data[0]["gdp"] == 25462.0


def test_average_gdp_report(sample_csv_file):
    data = parse_csv_files(sample_csv_file)
    report = AverageReport(data)
    result = report.generate_report()
    assert "United States" in result
    assert "23923.67" in result
