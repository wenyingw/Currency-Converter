import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    # => To be filled by student
    try to get response from input endpoint
    if no error
        then
            return response(api response)
    if error occur
        then
            return response(error string)

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    # => To be filled by student
    try:
        response = requests.get(url)
    except:
        response = 'There is an error with API call'
    return response
    

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student

    currencies_url = concatenate strings _HOST_ and _CURRENCIES_
    return currencies_url

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    # => To be filled by student
    currencies_url = _HOST_ + _CURRENCIES_
    return currencies_url


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student
    if call_api success
        then
            assign dictionary format of response get by call_api to resp_dict
            extract all keys in resp_dict to a list resp_list
            return resp_list
    if call_api occurs error
        then
            return error message returned by call_api

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # => To be filled by student
    if not type(call_api(format_currencies_url())) is str:
        resp_dict = call_api(format_currencies_url()).json()
        resp_list = [i for i in resp_dict]
        return resp_list
    return call_api(format_currencies_url())


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    # => To be filled by student
    latest_url = concatenate from_currency & to-currency into the url format the API accept 
    return latest_url
    
    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # => To be filled by student
    latest_url = _HOST_ + _LATEST_ + '?from='+ from_currency +'&to=' + to_currency
    return latest_url

