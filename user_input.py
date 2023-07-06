import config

class UserCommunication:
    '''Get input from user and return amount, source currency and target currency for exchange'''

    def get_user_input(self):
        
        # user_input error handling - if input string or negative value 
        amount = 0
        while amount <= 0:
            try:
                amount = float(input("Enter the amount you wish to convert: "))
                if amount <= 0:
                    print('Please provide a number greater than 0')
            except ValueError:
                print('Provided value is not a number. Please provide a valid number as the amount')

        # Source and target currency input format - if the currency in the API data list from SUPPORTED_CURRENCIES(hard coded in line 6), it is acccepted and if not exception raised for source and target curiencies.
        source_currency = None
        while source_currency is None:
            user_provided_source_currency = input("Enter the source currency (e.g., USD, EUR, GBP, JPY): ")
            if user_provided_source_currency in config.SUPPORTED_CURRENCIES:
                source_currency = user_provided_source_currency
            else:
                print('Provided source currency is not valid or not supported. Please provide a supported currency from: ' + str(config.SUPPORTED_CURRENCIES))

        target_currency = None
        while target_currency is None:
            user_provided_target_currency = input("Enter the target currency (e.g., USD, EUR, GBP, JPY): ")
            if user_provided_target_currency in config.SUPPORTED_CURRENCIES:
                target_currency = user_provided_target_currency
            else:
                print('Provided target currency is not valid or not supported. Please provide a supported currency from: ' + str(config.SUPPORTED_CURRENCIES))

        return amount, source_currency, target_currency