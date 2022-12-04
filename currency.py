from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    # => To be filled by student
    if no api error occurs
        then 
            currency_list = result of get_currencies
            if upper case of currency is in currency_list:
                then
                    return True
            if upper case of currency is not in currency_list:
                then
                    return False
    if api error occurs
        then
            return error message returned by call_api

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    # => To be filled by student    
    if type(get_currencies()) is list:
        currency_list = get_currencies()
        if currency.upper() in currency_list:
            return True
        return False
    return get_currencies()


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # => To be filled by student
        self.inverse_rate = format(1 / self.rate, '.5f')

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        # => To be filled by student
        message = (f"Today's ({self.date}) conversion rate from {self.from_currency} to "
                    f"{self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}")
        return message
        


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    # => To be filled by student
    instantiate a Currency class - currency
    assign Currency class attributes according to input dictionary
    assign currency.inverse_rate by calling reverse_rate method

    Returns
    -------
    Currency
        Instantiated Currency
    """
    # => To be filled by student
    currency = Currency()
    currency.from_currency = result.get('base')
    currency.to_currency = list(result.get('rates'))[0]
    currency.amount = result.get('amount')
    currency.rate = result.get('rates').get(currency.to_currency)
    currency.date = result.get('date')
    currency.reverse_rate()
    return currency
    
