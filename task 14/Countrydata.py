import requests     # 'Requests' module used to make the HTTP requests 

class Country:      # Country class created
    def __init__(self, url):    # Construtor inititated to fetch the json.data
        self.url = url
        self.data = self.json_data()

    def json_data(self):   # JSON Data Retrieval method.
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"{response.status_code}")
            return None

    def country_details(self):      # Function to display the country details.
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A') # Get the country name from the url
            currencies = country.get('currencies', {})          # Get the currency list from the url
            currency_names = [info.get('name', 'N/A') for info in currencies.values()]  # Get the currency name from the url
            currency_symbols = [info.get('symbol', 'N/A') for info in currencies.values()]  # Get the currency symbol from the url

            print(f"Country: {name}")       # Display the country name.
            print(f"Currencies: {', '.join(currency_names)}")   # Display the currency name.
            print(f"Currency Symbols: {', '.join(currency_symbols)}")   # Display the currency symbol.
            print("-" * 40)     # Line separation between the each country.

    def dollar(self):       # Function to display the countries having dollar.
        dollar_countries = [country for country in self.data if 'USD' in country.get('currencies', {}).keys()]
        print("Countries with DOLLAR as currency:")
        for country in dollar_countries:
            print(country.get('name', {}).get('common', 'N/A')) # Display all the countries having dollar currency

    def euro(self):         # Function to display the countries having euro.
        euro_countries = [country for country in self.data if 'EUR' in country.get('currencies', {}).keys()]
        print("Countries with EURO as currency:")
        for country in euro_countries:
            print(country.get('name', {}).get('common', 'N/A')) # Display all the countries having euro currency

url = "https://restcountries.com/v3.1/all"  # Given url to fetch the country details
obj = Country(url)    # Call the country function to get the data
obj.country_details() # Display all country information
obj.dollar() # Display countries with DOLLAR as currency
obj.euro()   # Display countries with EURO as currency
