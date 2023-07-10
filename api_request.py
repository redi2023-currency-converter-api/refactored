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

        # throwing resulting errors to the caller
        response.raise_for_status()

        # getting the payload 
        data = response.json()
        
        assert 'data' in data, 'Malformed json response from the REST API. The element \'data\' not found'
        rates = data['data']

        assert target_currency in rates, 'Target currency is not supported by the API'
             
        return rates[target_currency]
    