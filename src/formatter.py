from tabulate import tabulate

def format_report(data):
    return tabulate(data, headers='keys', tablefmt='pretty')
