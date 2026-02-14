import argparse
from parser import parse_csv_files
from reports import report_factory


def main():
    parser = argparse.ArgumentParser(description='Генерация отчетов по экономическим данным')
    parser.add_argument('--files', type=str, nargs='+', required=True, help='Пути к CSV файлам')
    parser.add_argument('--report', type=str, default='average-gdp', help='Тип отчета (average-gdp по умолчанию)')
    args = parser.parse_args()

    try:

        data = parse_csv_files(args.files)
        report = report_factory(args.report, data)
        print(report.generate_report())


    except Exception as e:
        print(f"Ошибка при выполнении: {e}")


if __name__ == '__main__':
    main()
