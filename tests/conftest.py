import pytest
import os
import csv

@pytest.fixture
def sample_csv_file(tmp_path):
    data = [
        {"country": "United States", "gdp": 25462, "year": 2023},
        {"country": "United States", "gdp": 23315, "year": 2022},
        {"country": "United States", "gdp": 22994, "year": 2021},
        {"country": "China", "gdp": 17963, "year": 2023},
        {"country": "China", "gdp": 17734, "year": 2022},
        {"country": "China", "gdp": 17734, "year": 2021},
        {"country": "Germany", "gdp": 4086, "year": 2023},
        {"country": "Germany", "gdp": 4072, "year": 2022},
        {"country": "Germany", "gdp": 4257, "year": 2021}
    ]
    file_path = os.path.join(tmp_path, "economic1.csv")
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    data2 = [
        {"country": "Germany", "gdp": 4086, "year": 2023},
        {"country": "Germany", "gdp": 4072, "year": 2022},
        {"country": "Germany", "gdp": 4257, "year": 2021},
        {"country": "China", "gdp": 17963, "year": 2023},
        {"country": "China", "gdp": 17734, "year": 2022},
        {"country": "China", "gdp": 17734, "year": 2021},
        {"country": "United States", "gdp": 25462, "year": 2023},
        {"country": "United States", "gdp": 23315, "year": 2022},
        {"country": "United States", "gdp": 22994, "year": 2021}
    ]
    file_path2 = os.path.join(tmp_path, "economic2.csv")
    with open(file_path2, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data2[0].keys())
        writer.writeheader()
        writer.writerows(data2)

    return [file_path, file_path2]
