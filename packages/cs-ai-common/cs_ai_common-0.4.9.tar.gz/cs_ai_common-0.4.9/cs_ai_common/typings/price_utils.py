from enum import StrEnum


class PriceCurrency(StrEnum):
    PLN = 'PLN'
    EUR = 'EUR'

    @staticmethod
    def to_common(value: str) -> 'PriceCurrency':
        value = value.upper()
        if value == 'PLN':
            return PriceCurrency.PLN
        
        if value == 'EUR':
            return PriceCurrency.EUR

        raise ValueError(f'Invalid value: {value}')