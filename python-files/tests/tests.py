from main import get_stock_websites

def test_get_stock_websites():
    stock_names = ['RELIANCE', 'TCS', 'INFY']
    expected_output = {
        'RELIANCE': 'https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE',
        'TCS': 'https://www.nseindia.com/get-quotes/equity?symbol=TCS',
        'INFY': 'https://www.nseindia.com/get-quotes/equity?symbol=INFY'
    }
    assert get_stock_websites(stock_names) == expected_output