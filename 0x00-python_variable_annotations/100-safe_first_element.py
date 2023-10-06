#!usr/bin/env python3
"""correct duck-typed annotations of
ef safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
        """
from typing import Sequence, Optional, TypeVar

T = TypeVar('T')

def safe_first_element(lst: Sequence[T]) -> Optional[T]:
    """
    Safely retrieve the first element of an iterable with an optional default.

    Args:
        lst (Sequence[T]): The iterable from which to retrieve the first element.

    Returns:
        Optional[T]: The first element of the iterable, or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

