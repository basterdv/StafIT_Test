import csv


def parse_csv_files(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "country": row["country"],
                    "gdp": float(row["gdp"]),
                })
    return data
