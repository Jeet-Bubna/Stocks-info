from pythonfiles.main import get_stock_websites, scrape_data

# Tip: run python -m pythonfiles.tests.tests and not the other commands

def test_get_stock_websites():
    stock_names = ['RELIANCE', 'TCS', 'INFY']
    expected_output = {
        'RELIANCE': 'https://zerodha.com/markets/stocks/NSE/RELIANCE',
        'TCS': 'https://zerodha.com/markets/stocks/NSE/TCS',
        'INFY': 'https://zerodha.com/markets/stocks/NSE/INFY'
    }
    assert get_stock_websites(stock_names) == expected_output

def scrape_data_test():
    url = 'https://zerodha.com/markets/stocks/NSE/TCS'
    stock_name = 'TCS'
    data = scrape_data(url, stock_name)
    assert isinstance(data, dict)  # Check if the returned data is a dictionary
    assert 'PE' in data  # Check if 'PE' key is in the returned dictionary
    assert 'Sector PE' in data  # Check if 'Sector PE' key is in the returned dictionary
    assert 'PB Ratio' in data  # Check if 'PB Ratio' key is in the returned dictionary
    assert 'Div Yield' in data  # Check if 'Div Yield' key is in the returned dictionary
    assert 'ROE' in data  # Check if 'ROE' key is in the returned dictionary
    assert 'EBIDATA' in data  # Check if 'EBIDATA' key is in the returned dictionary
    assert 'ROCE' in data  # Check if 'ROCE' key is in the returned dictionary
    assert 'EPS' in data  # Check if 'EPS' key is in the returned dictionary


def test_all():
    try:
        test_get_stock_websites()
        print(f"test_get_stock..... ✅")
    except AssertionError as e:
        print(f"test_get_stock..... ❌: {e}")
    
    try:
        scrape_data_test()
        print(f"scrape_data........ ✅")
    except AssertionError as e:
        print(f"scrape_data........ ❌: {e}")
    
    print('All tests conducted')
