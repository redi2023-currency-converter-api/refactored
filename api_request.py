import requests
import config

class ExchangeRate():
    '''Create an API-request and get exchange rate for target currency'''
    
    def get_exchange_rate(self, source_currency, target_currency):
        params = {
            'apikey': config.API_KEY,
            'base_currency': source_currency,
            }

        response = requests.get(config.BASE_URL, params=params)
        ### handling HTTP response headers. See https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        # HTTP handling in API necessary documented in API documentation. See https://freecurrencyapi.com/docs/#authentication-methods

        if response.status_code == 401:
            raise Exception('API authentication failed. Invalid API key provided. Unable to access the API')

        if response.status_code == 429:
            raise Exception('API quota rate limit reached. API refused connection. Please wait')

        if response.status_code != 200:
            raise Exception('Error while connecting to the API. Giving up')

        data = response.json()

        if 'data' not in data:
            raise Exception('Error while fetching data from the API. No data received')

        rates = data['data']

        if target_currency not in rates:
            raise Exception(f"Provided 'target_currency' {target_currency} is not found in the API response")

        return rates[target_currency]
    