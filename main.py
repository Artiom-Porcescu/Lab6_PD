import unittest
from datetime import datetime
from currency_data import get_data_for_date

class TestCurrencyData(unittest.TestCase):
    # Тестирование возвращения корректного значения курса валюты на заданную дату
    def test_get_data_for_date_valid(self):
        test_file = 'dataset.csv'
        test_date = datetime.strptime('2023/09/01', '%Y/%m/%d')
        result = get_data_for_date(test_date, test_file)
        self.assertAlmostEqual(result, 96.3344)

    # Тестирование возвращения None при отсутствии данных о курсе валюты на заданную дату
    def test_get_data_for_date_invalid(self):
        test_file = 'dataset.csv'
        test_date = datetime.strptime('2023/11/01', '%Y/%m/%d')
        result = get_data_for_date(test_date, test_file)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
