#!/usr/bin/env python3
"""Return a Tuple from two arguments"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string 'k' and the square of 'v' as a float.

    Args:
        k (str): The string 'k'.
        v (Union[int, float]): An integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing 'k' and the square of 'v' as a float.
    """
    squared_value = float(v) ** 2
    return k, squared_value
