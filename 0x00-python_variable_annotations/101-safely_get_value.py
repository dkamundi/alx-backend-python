#!/usr/bin/env python3
"""Type annonate using TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Safely retrieve a value from a dictionary with an optional default."""
    if key in dct:
        return dct[key]
    else:
        return default

