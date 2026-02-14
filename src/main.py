import argparse
from src.parser import parse_csv_files
from src.reports import report_factory


def main():
    parser = argparse.ArgumentParser(description='Генерация отчетов по экономическим данным')
    parser.add_argument(
        '--files',
        type=str,
        nargs='+',
        required=True,
        help='Пути к CSV файлам'
    )
    parser.add_argument(
        '--report',
        type=str,
        default='average-gdp',
        nargs='?',
        const='average-gdp',
        help='Тип отчета (average-gdp по умолчанию)'
    )
    args = parser.parse_args()

    try:

        data = parse_csv_files(args.files)
        if not data:
            print("Ошибка: Файлы пусты или не найдены.")
            return

        report = report_factory(args.report, data)
        if not report:
            print("Ошибка формирования отчета.")
            return

        print(report.generate_report())

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден — {e}")
    except PermissionError:
        print("Ошибка: Нет прав на чтение одного из файлов.")
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")


if __name__ == '__main__':
    main()
