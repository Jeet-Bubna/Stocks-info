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

    #Checks if the keys are present in the response
    assert isinstance(data, dict) 
    assert 'PE' in data 
    assert 'Sector PE' in data 
    assert 'PB Ratio' in data 
    assert 'Div Yield' in data  
    assert 'ROE' in data  
    assert 'EBIDATA' in data 
    assert 'ROCE' in data  
    assert 'EPS' in data  


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
