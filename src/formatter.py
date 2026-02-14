from tabulate import tabulate


def format_report(data):
    if not data:
        return print("Нет данных для формирования таблицы.")

    return tabulate(
        data,
        headers='keys',
        tablefmt='pretty',
        numalign="right",
        stralign="left",
    )
