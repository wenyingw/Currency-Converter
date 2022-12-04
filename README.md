# Currency Converter
## Description
The app is built for currency conversion using data fetched from an open-source API. The program generates rate and inverse rate between exactly 2 currencies.
The input error message will be displayed when the number of input currency codes is not equal to 2.
Validation error message will be displayed when 1 or more input currency code is not valid.
API error message will be displayed when an API error is encountered.

## Available Commands

In the project directory, you can run:

- `python main.py AUD EUR` or `python main.py aud euR`  
	- Program will return: "AUD to EUR rate and the inverse rate (if and only if 2 inputs are valid inputs)"
- `python main.py`, `python main.py AUD`, `python main.py AUD EUR CNY` etc. 
	- If number of input is not equal to 2,  program will return: "Error message: [ERROR] You haven't provided 2 currency codes"
- `python main.py usd AAA`, `python main.py AAA usd` etc.
	- Program will return: "AAA is not a valid option"
- `python main.py BBB AAA`
	- program will return: "BBB and AAA are not valid options"
- When encounter API error
	- Program will return: "There is an error with API call"

If you are using Pipenv, then you can run:

- `pipenv python main.py AUD EUR`

## Built With

- Python 3.9.6

## Package Dependencies

- requests

## Structure

    ├── api.py             <- python script that will contain the code for calling API endpoints
    ├── currency.py        <- python script that will contain the code for checking if currency code is valid, store results and format final output
    ├── main.py            <- main program used for entering the input parameters (currency codes)      and display the results
    ├── Pipfile            <- not used
    ├── Pipfile.lock       <- not used
    ├── README.md          <- a markdown file containing aurthor details (full name, student id), a description of this project, listing of all Python functions and classes and instructions for running your code 
    ├── test_api.py        <- python script for testing code from api.py
    └── test_currency.py   <- python script for testing code from currency.py


<sub><sup>Edit on Sep 09, 2021</sup></sub>