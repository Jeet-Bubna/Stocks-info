# main.py 
# Author: Jeet Bubna

def scrape_data(url: str) -> float:
    
    """
    Given a url, scrape the data from the website and return the price of the stock.
    Args:
        url (str): The url of the stock website.
    Returns:
        float: The price of the stock.
    

    First, we need to send a request to the url to get the html content.
    The NSE has done some shit which doesnt let webscraping happen easily
    So we just change the headers such that it doesnt show that we are doing
    It using a python script. Requests library like has one of its headers
    Blasting that it is a python script. The website just blocks ts 😭😭

    """

    # Getting the html code
    import requests as rq
    data = rq.get(url=url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'})

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text, 'html.parser')
    soup.prettify()


    price = soup.find_all('div', class_='blkbox-whitetxt')
    print(price)

    #TODO: find out why the price isnt appearing when scraping data - where the price is supposed to be, it isnt showing! Simply! idk why check out once

    # Parse it

def get_stock_websites(stock_names: list) -> dict:

    """
    Given a list of stock names, return a dictionary mapping each stock name to its website.
    For now, it only works with the exact name of the stock. The default URL is
    URL = 'https://www.nseindia.com/get-quotes/equity?symbol='
    Args:
        stock_names (list): A list of stock names.
    Returns:
        dict: A dictionary where keys are stock names and values are their nse website which are needed to be scraped from.
    """

    def get_url(stock_name: str) -> str:
        URL = 'https://www.nseindia.com/get-quotes/equity?symbol='
        return URL + stock_name.upper()

    #Dict comprehension, faster than for loop, but less readable lmao
    return {stock_name: get_url(stock_name) for stock_name in stock_names} 

def main():

    # Get stock names from user

    num_stocks = int(input("Enter the number of stocks: "))
    stock_names = []
    for _ in range(num_stocks):
        stock_name = input("Enter stock name: ")
        stock_names.append(stock_name)

    # Get the websites of the stocks

    stock_websites = get_stock_websites(stock_names)

    # Scrape the data to get prices
    
    data = {}
    for ctr in range(len(stock_websites) - 1):
        price = scrape_data(stock_websites[ctr])
        data.update({stock_names[ctr]: price})      # The index of the stock remains unchanged

    # Do something with the data, here just printing it

    print(data)

if __name__ == "__main__":
    main()