#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator



async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[int]: A list of 10 random numbers.
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
