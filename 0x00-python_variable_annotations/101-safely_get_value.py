#!/usr/bin/env python3
"""correct duck-typed annotations of

def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import Dict, TypeVar, Optional

V = TypeVar('V')


def safely_get_value(dct: Dict[str, V], key: str, default: Optional[V] = None) -> V:
    """Safely retrieve a value from a dictionary with an optional default."""
    if key in dct:
        return dct[key]
    else:
        return default
