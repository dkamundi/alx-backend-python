#!/usr/bin/env python3
"""Returns sum of an array"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats to be summed.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
