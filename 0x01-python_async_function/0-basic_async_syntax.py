#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay waited in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


if __name__ == "__main__":
    asyncio.run(wait_random())
