from pythonfiles.main import get_stock_websites, scrape_data

# Tip: run python -m pythonfiles.tests.tests and not the other commands

def test_get_stock_websites():
    stock_names = ['RELIANCE', 'TCS', 'INFY']
    expected_output = {
        'RELIANCE': 'https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE',
        'TCS': 'https://www.nseindia.com/get-quotes/equity?symbol=TCS',
        'INFY': 'https://www.nseindia.com/get-quotes/equity?symbol=INFY'
    }
    assert get_stock_websites(stock_names) == expected_output

def test_scrape_data(url: str):
    expcted_output = '3,054.70'  # Replace with the actual expected price for RELIANCE
    assert scrape_data(url) == expcted_output

test_scrape_data('https://www.nseindia.com/get-quotes/equity?symbol=TCS')