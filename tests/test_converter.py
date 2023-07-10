import pytest
from main import CurrencyConverter
from api_request import ExchangeRate
from user_input import UserCommunication

def test_convert_happy_path():
    expected_result = 198.111234108
    cc = CurrencyConverter()
    result = cc.convert(user_input = [2, 'EUR', 'RUB'])
    assert result == expected_result

def test_get_exchange_rate_happy_path():
    expected_result = 99.055617054
    ex = ExchangeRate()
    result = ex.get_exchange_rate('EUR', 'RUB')
    assert result == expected_result

def test_get_exchange_rate_error_input():
    ex = ExchangeRate()
    with pytest.raises(Exception):
        ex.get_exchange_rate(324, 'EUR')

def test_get_exchange_rate_empty_input():
    ex = ExchangeRate()
    with pytest.raises(Exception):
        ex.get_exchange_rate()