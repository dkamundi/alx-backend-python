#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.
"""

import asyncio
import random
from typing import List

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

async def wait_n(n: int, max_delay: int) ->List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    coroutines = [wait_random(max_delay) for _ in range(n)]
    awaitables = asyncio.gather(*coroutines)
    results = await awaitables
    results = await awaitables
    delays.extend(results)
    delays.sort()
    return delays
