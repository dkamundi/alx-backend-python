#!/usr/bin/env python3
"""
measure the total runtime and return it.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather
    and measure the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    # Start a timer
    start_time = time.perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())

    # Stop the timer
    end_time = time.perf_counter()

    # Calculate and return the total runtime
    total_runtime = end_time - start_time
    return total_runtime
