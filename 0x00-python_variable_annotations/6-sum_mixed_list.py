#!/usr/bin/env python3
"""Returns sum of a mixed array"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to be summed.

    Returns:
        float: The sum of the integers and floats in the input list as a float.
    """
    return sum(mxd_lst)
