from enum import StrEnum

_TRANSMISIONS_AUTO = ['automatic', 'automatic_transmission', 'automatyczna']
_TRANSMISIONS_MANUAL = ['manual', 'manual_transmission', 'manualna']

class Transmisions(StrEnum):
    AUTO = 'automatic'
    MANUAL = 'manual'

    @staticmethod
    def to_common(value: str) -> 'Transmisions':
        value = value.lower()
        if value in _TRANSMISIONS_MANUAL:
            return Transmisions.MANUAL
        
        if value in _TRANSMISIONS_AUTO:
            return Transmisions.AUTO
        
        raise ValueError(f'Invalid value: {value}')


class FuelTypes(StrEnum):
    PETROL = 'petrol'
    PETROL_CNG = 'petrol_cng'
    PETROL_LPG = 'petrol_lpg'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'
    ETHANOL = 'ethanol'
    HYBRID = 'hybrid'
    PLUGIN_HYBRID = 'plugin_hybrid'
    HYDROGEN = 'hydrogen'

    @staticmethod
    def to_common(value: str) -> 'FuelTypes':
        value = value.lower().replace('-', '_')
        enum_value = FuelTypes.__members__.get(value.upper())

        if enum_value:
            return enum_value
        
        if _is_exceptional(value):
            return _exceptional_value_to_common(value)

        raise ValueError(f'Invalid value: {value}')
    

def _is_exceptional(value: str) -> bool:
    return value in ['petrol_lpg', 'lpg_petrol', 'lpg', 'cng', 'hybrid']

def _exceptional_value_to_common(value: str) -> FuelTypes:
    is_lpg = 'lpg' in value
    if is_lpg:
        return FuelTypes.PETROL_LPG
    
    is_hybrid_plugin = 'hybrid' in value
    if is_hybrid_plugin:
        return FuelTypes.PLUGIN_HYBRID
    
    is_cng = 'cng' in value
    if is_cng:
        return FuelTypes.PETROL_CNG
    
    raise ValueError(f'Invalid exceptional value: {value}')