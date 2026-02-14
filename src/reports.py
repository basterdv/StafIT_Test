from collections import defaultdict
from src.formatter import format_report


class AverageReport():
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        country_gdp = defaultdict(list)
        for row in self.data:
            country_gdp[row['country']].append(row['gdp'])

        # расчет средних значений
        average_gdp = [
            {
                "country": country
                , "gdp": sum(gdps) / len(gdps)
            }
            for country, gdps in country_gdp.items()
        ]

        # сортируем числа
        average_gdp.sort(key=lambda x: x['gdp'], reverse=True)

        # превращаем числа с 0.00 и добавляем нумерацию строк
        final_data = []
        for i,item in enumerate(average_gdp,1):
            final_data.append({
                "№": i,
                "country": item["country"],
                'gdp': f"{item['gdp']:.2f}"
            })

        return format_report(final_data)


def report_factory(report_type, data):
    if report_type:
        return AverageReport(data)
    else:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")
