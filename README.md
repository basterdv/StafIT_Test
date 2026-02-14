

Структура проекта

StafIT_Test/
├── data/                   # Примеры или сырые CSV файлы
│   ├── economic1.csv
│   └── economic1.csv
├── src/                    # Исходный код
│   ├── __init__.py
│   ├── main.py             # Точка входа (argparse и запуск логики)
│   ├── parser.py           # Логика чтения и валидации CSV
│   ├── reports.py          # Реализация стратегий отчетов (BaseReport, AverageGDPReport)
│   └── formatter.py        # Обертка над tabulate для вывода
├── tests/                  # Тесты (pytest)
│   ├── __init__.py
│   ├── conftest.py         # Фикстуры (например, создание временных CSV)
│   └── test_reports.py     # Тесты логики расчетов
├── requirements.txt        # Зависимости (tabulate, pytest)
├── README.md               # Документация по запуску
└── .gitignore
