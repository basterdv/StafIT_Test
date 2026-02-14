# О проекте

 - Тестовое задание python junior. 2026.
 - Анализ макроэкономических данных


## Структура проекта
```
StafIT_Test/
├── data/                   # CSV файлы
│   ├── economic1.csv
│   └── economic1.csv
├── src/                    # Исходный код
│   ├── __init__.py
│   ├── main.py             # Точка входа 
│   ├── parser.py           # Логика чтения и валидации CSV
│   ├── reports.py          # Реализация отчетов 
│   └── formatter.py        # tabulate для вывода
├── tests/                  # Тесты (pytest)
│   ├── __init__.py
│   ├── conftest.py         # Фикстуры (создание временных CSV)
│   └── test_reports.py     # Тесты логики расчетов
├── requirements.txt        # Зависимости (tabulate, pytest)
├── README.md               # Документация по запуску
└── .gitignore
```

## Как запустить

### Базовый запуск (использует название отчета по умолчанию 'average-gdp')
```
python -m src.main --files data/economic1.csv data/economic2.csv
```

### С кастомным заголовком колонки
```
python -m src.main --files data/economic1.csv --report average_GDP
```

### Запуск тестов
```
pytest tests/
```
