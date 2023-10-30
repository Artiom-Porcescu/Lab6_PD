import csv
from datetime import datetime

def get_data_for_date(date, filename):

    """
    Извлекает данные из файла на основе указанной даты.

    Args:
        date (datetime): Дата для поиска в формате datetime.
        filename (str): Имя файла с данными в формате 'YYYY/MM/DD, rate'.

    Returns:
        float or None: Возвращает значение курса (rate) на указанную дату. Если данных нет, возвращает None.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Пропускаем первую строку, которая считается заголовком
        for row in reader:
            row_date = datetime.strptime(row[0], '%Y/%m/%d')  # Предполагается, что дата в первом столбце
            if row_date == date:
                return float(row[1])  # Возвращаем курс валюты (предположим, что он находится во втором столбце)
    return None

def get_currency_rate(date, filename):
    """
    Возвращает курс валюты USD на указанную дату из файла.

    Args:
        date (datetime): Дата.
        filename (str): Имя файла с данными в формате 'YYYY/MM/DD, rate'.

    Returns:
        float or None: Курс валюты USD на указанную дату. Если данные отсутствуют, возвращает None.
    """
    return get_data_for_date(date, filename)


def get_available_currencies():
    """
    Возвращает список доступных валют.

    Returns:
        list: Список строк с кодами доступных валют. Здесь возвращается только 'USD'.
    """
    return ['USD']
