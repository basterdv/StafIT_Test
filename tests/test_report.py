import pytest
from src.parser import parse_csv_files
from src.reports import AverageReport, report_factory

def test_parse_csv_files(sample_csv_file):
    data = parse_csv_files(sample_csv_file)
    assert len(data) == 9
    assert data[0] == {"country": "United States", "gdp": 25462.0, "year": 2023}
    assert data[5] == {"country": "China", "gdp": 17734.0, "year": 2022}

def test_average_gdp_report(sample_csv_file):
    data = parse_csv_files(sample_csv_file)
    report = AverageReport(data)
    result = report.generate_report()
    assert "United States" in result
    assert "23923.67" in result  # Среднее значение GDP для США из sample_csv_file

def test_report_factory(sample_csv_file):
    data = parse_csv_files(sample_csv_file)
    report = report_factory('average-gdp', data)
    assert isinstance(report, AverageReport)

    with pytest.raises(ValueError):
        report_factory('unknown-report', data)
