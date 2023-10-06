#!/usr/bin/env python3
"""Returns a function that multiplies a float"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier


    return multiplier_function
