import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student
    store inputs in args
    if number of input is not equal to 3
        then
            print error message
    else 
        then
            assign input values to from_currency and to_currency
            return print result of get_rate

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student
    # Check for length of inputs
    # Assumes only 2 input is deemed correct and process main(), 
    # otherwise return the same error message
    args = sys.argv[:]
    if len(args) != 3:
        return print("[ERROR] You haven't provided 2 currency codes")
    
    # assign values to be used for get_rate()
    from_currency = args[1]
    to_currency = args[2]
    
    # Check for types of inputs, not necessary
    # if not type(from_currency) is str:
    #     return print(f'{type(from_currency)} is not a valid option')
    # elif not type(to_currency) is str:
    #     return print(f'{type(to_currency)} is not a valid option')

    return print(get_rate(from_currency, to_currency))





def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    # => To be filled by student
    if both from_currency and to_currency are valid
        then
            if no api error occur
                then 
                    assign dictionary format of result of call_api to resp_latest
                    instantiate Currency as currency using extract_api_result
                    return result of currency's call format_result method
    if not both from_currency and to_currency are valid
        then
            if both from_currency and to_currency are not valid
                then
                    return corresponding error message
            if one of from_currency and to_currency is not valid
                then
                    return corresponding error message

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student
    if check_valid_currency(from_currency) and check_valid_currency(to_currency):
        # Format required url according to input currencies and store in lastest_url
        # Then call an API requesr and store result in resp_latest
        if not type(call_api(format_latest_url(from_currency, to_currency))) is str:
            resp_latest = call_api(format_latest_url(from_currency, to_currency)).json()
            currency = extract_api_result(resp_latest)
            return currency.format_result()
        
    else:
        if not check_valid_currency(from_currency) and not check_valid_currency(to_currency):
            return f'{from_currency} and {to_currency} are not valid options'
        if check_valid_currency(from_currency):
            return f'{to_currency} is not a valid option'
        if check_valid_currency(to_currency):
            return f'{from_currency} is not a valid option'


    


if __name__ == "__main__":
    main()
