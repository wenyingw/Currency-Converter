import unittest
from currency import check_valid_currency, extract_api_result, Currency

class TestValidCurrency(unittest.TestCase):
    def test_function(self):
        # => To be filled by student

        # 1. Test success uppercase 
        expected_1 = True
        result_1 = check_valid_currency('AUD')

        # 2. Test sucess lowercase
        expected_2 = True
        result_2 = check_valid_currency('aud')

        # 3. Test invalid input
        expected_3 = False
        result_3 = check_valid_currency('abc')

        self.assertEqual(expected_1, result_1) #1
        self.assertEqual(expected_2, result_2) #2
        self.assertEqual(expected_3, result_3) #3


class TestExtractApi(unittest.TestCase):
    def test_function(self):
        # => To be filled by student

        # Set static test case according to AUD to USD convertion rate on 2021-09-08

        test_dict = {'amount': 1.0, 'base': 'AUD', 'date': '2021-09-08', 'rates': {'USD': 0.73794}}
        result_class = extract_api_result(test_dict)
        expected_string = (f"Today's (2021-09-08) conversion rate from AUD to "
                    f"USD is 0.73794. The inverse rate is 1.35512")
        #test extract_api_result & Currency by testing all the attributes and methods
        self.assertEqual(result_class.from_currency, 'AUD')
        self.assertEqual(result_class.to_currency, 'USD')
        self.assertEqual(result_class.amount, 1.0)
        self.assertEqual(result_class.rate, 0.73794)
        self.assertEqual(result_class.inverse_rate, '1.35512')
        self.assertEqual(result_class.date, '2021-09-08')
        self.assertEqual(result_class.format_result(), expected_string)

