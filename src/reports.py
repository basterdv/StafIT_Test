from collections import defaultdict
from src.formatter import format_report


class BaseReport:
    def __init__(self, data):
        self.data = data


class AverageReport(BaseReport):
    def generate_report(self):
        country_gdp = defaultdict(list)
        for row in self.data:
            country_gdp[row['country']].append(row['gdp'])

        average_gdp = [
            {"country": country, "gdp": sum(gdps) / len(gdps)}
            for country, gdps in country_gdp.items()
        ]
        average_gdp.sort(key=lambda x: x['gdp'], reverse=True)
        return format_report(average_gdp)


def report_factory(report_type, data):
    if report_type == 'average-gdp':
        return AverageReport(data)
    else:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")
