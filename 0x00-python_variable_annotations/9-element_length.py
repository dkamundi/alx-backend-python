#!/usr/bin/env python3
"""Annonating the following


>>>def element_length(lst):
>>>  return [(i, len(i)) for i in lst]
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the input list.
    """
    return [(i, len(i)) for i in lst]
