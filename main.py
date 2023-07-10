from user_input import UserCommunication
from api_request import ExchangeRate
import requests

class CurrencyConverter:
#Create a currency converter function using user unput and exchange rate from the API

    def convert(self, user_input):
        # Create a variable that store the currency exchange change rate from the API
        rate = ExchangeRate()
        exchange_rate = rate.get_exchange_rate(user_input[1], user_input[2])
        # Convert by multiplying the amount to the target currency exchange rate
        return user_input[0] * exchange_rate


def main():
    # Create an object of class CurrencyConverter
    converter = CurrencyConverter()
    user_communication = UserCommunication()
    # Call the get_user_input function and the values returned will store in the user_input variable (tuple)
    user_input = user_communication.get_user_input()

    try:
        # Call the convert function and the value returned will stored in output variable, limit the precision to 2 decimal places
        output = round(converter.convert(user_input), 2)
        
        # Print the output
        print(f"{user_input[0]} {user_input[1]} is equivalent to {output} {user_input[2]}.")
        return output
    
    except requests.exceptions.ConnectionError as e:
        print('Network error. Unable to call the REST API: ', e)

    except requests.exceptions.HTTPError as e:
        print('The REST API returned an error: ', e)

    except requests.exceptions.RequestException as e:
        print('Error while connecting to the REST API:', e)
    
    except AssertionError as e:
        print(e)

    except Exception as e:
        print('Unable to convert the currency. Program ran into an error:', e)


if __name__ == '__main__':
    main()
