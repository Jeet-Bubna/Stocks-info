# main.py 
# Author: Jeet Bubna

def scrape_data(url: str) -> float:
    pass

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