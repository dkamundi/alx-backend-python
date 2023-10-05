#!/usr/bin/env python3
"""Annonating the following

def element_length(lst):
  return [(i, len(i)) for i in lst]
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (List[str]): The list of strings for which the length of each element is calculated.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a string from the input
        list and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
