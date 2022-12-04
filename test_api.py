import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_function(self):
        # => To be filled by student
        
        # 1. Test for format_currencies_url
        expected_currencies_url = _HOST_ + _CURRENCIES_
        result_currencies_url = format_currencies_url()

        # 2. Test for format_latest_url
        from_currency = 'AAA'
        to_currency = 'BBB'
        expected_latest_url_correct = 'https://api.frankfurter.app/latest?from=AAA&to=BBB'
        result_latest_url_correct = format_latest_url(from_currency, to_currency)
        # 3. Test the order of inputs
        expected_latest_url_wrong = 'https://api.frankfurter.app/latest?from=BBB&to=AAA'
        result_latest_url_wrong = format_latest_url(to_currency, from_currency)

        self.assertEqual(expected_currencies_url, result_currencies_url) #1
        self.assertEqual(expected_latest_url_correct, result_latest_url_correct) #2
        self.assertEqual(expected_latest_url_wrong, result_latest_url_wrong) #3


class TestAPI(unittest.TestCase):
    def test_function(self):
        # => To be filled by student

        # 1. Test for call_api - success scenario
        expected_type_str = "<class 'requests.models.Response'>"
        result_type_str = str(type(call_api(format_currencies_url())))
        
        # 2. Test for call_api - error scenario
        expected_error = 'There is an error with API call'
        result_error = call_api('123456')

        # 3. Test for get_currencies 
        expected_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD',\
            'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP',\
            'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        result_list = get_currencies()

        self.assertEqual(expected_type_str, result_type_str) #1
        self.assertEqual(expected_error, result_error) #2
        self.assertEqual(expected_list, result_list) #3



