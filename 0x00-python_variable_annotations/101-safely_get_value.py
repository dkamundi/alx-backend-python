#!/usr/bin/env python3
"""correct duck-typed annotations of

def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import TypeVar, Dict, Any, Union 

K = TypeVar('K')


def safely_get_value(dct: Dict[K, Any], key: K, default: Union[Any, None] = None) -> Union[Any, None]:
    """Safely retrieve a value from a dictionary with an optional default."""
    if key in dct:
        return dct[key]
    else:
        return default

