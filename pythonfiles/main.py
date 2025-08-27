# main.py 
# Author: Jeet Bubna

def scrape_data(url: str, stock_name:str) -> float:
    
    """
    Given a url, scrape the data from the website and return the price of the stock.
    Args:
        url (str): The url of the stock website.
        stock_name (str): The name of the stock.
    Returns:
        float: The price of the stock.
    

    First, we need to send a request to the url to get the html content.
    The NSE has done some shit which doesnt let webscraping happen easily
    So we just change the headers such that it doesnt show that we are doing
    It using a python script. Requests library like has one of its headers
    Blasting that it is a python script. The website just blocks ts 😭😭
    
    UPDATE: This doenst seem to work, nor with any headless automation attempts
    redering this way obsolete. Hence, we use Zerodha to get the data, except
    price, because that has been redacted for some reason.

    """

    # Getting the html code
    import requests as rq
    data = rq.get(url=url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'})

    if data.status_code == 200:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text, 'html.parser')

        try:
            pe = soup.find_all('div', {'class': 'stat_value'})[0].text.strip()
            sector_pe = soup.find_all('div', {'class': 'stat_value'})[1].text.strip()
            pb_ratio = soup.find_all('div', {'class': 'stat_value'})[2].text.strip()
            div_yield = soup.find_all('div', {'class': 'stat_value'})[3].text.strip()
            roe = soup.find_all('div', {'class': 'stat_value'})[4].text.strip()
            ebidata = soup.find_all('div', {'class': 'stat_value'})[5].text.strip()
            roce = soup.find_all('div', {'class': 'stat_value'})[6].text.strip()
            eps = soup.find_all('div', {'class': 'stat_value'})[7].text.strip()
            return {'PE': pe, 'Sector PE': sector_pe, 'PB Ratio': pb_ratio, 'Div Yield': div_yield, 'ROE': roe, 'EBIDATA': ebidata, 'ROCE': roce, 'EPS': eps}
        except Exception as e:
            if e == IndexError:
                print(f"{stock_name} ❌ Error parsing data: {e} - Possibly changed website structure")
            else:
                print(f"{stock_name} ❌ Error parsing data: {e}")
            return 'N/A'
    else:
        print(f"{stock_name} ❌ HTTP Error: {data.status_code}")
        return 'N/A'


    

def get_stock_websites(stock_names: list) -> dict:

    """
    Given a list of stock names, return a dictionary mapping each stock name to its website.
    For now, it only works with the exact name of the stock. The default URL is
    URL = 'https://zerodha.com/markets/stocks/NSE/'
    Args:
        stock_names (list): A list of stock names.
    Returns:
        dict: A dictionary where keys are stock names and values are their nse website which are needed to be scraped from.
    """

    def get_url(stock_name: str) -> str:
        URL = 'https://zerodha.com/markets/stocks/NSE/'
        return URL + stock_name.upper()

    #Dict comprehension, faster than for loop, but less readable lmao
    return {stock_name: get_url(stock_name) for stock_name in stock_names} 

def main():
    """
    --------------------------------------------------------------------------
    NOTE: RUN THE FILE USING THE COMMAND
    python -m pythonfiles.main
    AND NOT python pythonfiles/main.py
    This is because of the relative imports used in the file.
    --------------------------------------------------------------------------
    """

    # For development, testing
    from pythonfiles.tests import tests
    tests.test_all()

    # Get stock names from user

    num_stocks = int(input("Enter the number of stocks: "))
    stock_names = []
    for _ in range(num_stocks):
        stock_name = input("Enter stock name (Symbol): ")
        stock_names.append(stock_name)

    # Get the websites of the stocks

    stock_websites = get_stock_websites(stock_names)

    # Scrape the data to get prices
    
    data = {}
    for stock_name, url in stock_websites.items():
        data[stock_name] = scrape_data(url, stock_name)
        if data[stock_name] == 'N/A':
            print(f"{stock_name} ❌ Error fetching data")

    # Do something with the data, here just printing it

    print(data)

if __name__ == "__main__":
    main()