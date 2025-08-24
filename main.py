def get_stocks_data(stock_list, API_KEY):
    import requests

    # DATA = {}
    # for stock in stock_list:
    #     url = f"https://example-finance-api.com/stock/{stock}?apikey={API_KEY}"
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         DATA[stock] = response.json()
    #     else:
    #         DATA[stock] = {"error": "Could not fetch data"}
    # return DATA

    # Placeholder function to simulate API call

def main():
    #Import libraries and API keys
    #--------------------------------
    import dotenv
    API_KEY = dotenv.get_key('API_KEY.env', 'API_KEY')

    #Input of user for which stocks to be fetched
    #--------------------------------
    stock_list = []

    number_of_stocks = int(input("Enter number of stocks to be fetched: "))
    for _ in range(number_of_stocks):
        stock_name = input("Enter stock name: ")
        stock_list.append(stock_name)

    #Call the API
    #--------------------------------

    DATA = get_stocks_data(stock_list, API_KEY)

    #Compile results
    #--------------------------------
    #Transfer to CSV


if __name__ == "__main__":
    main()