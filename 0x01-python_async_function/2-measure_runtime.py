#!/usr/bin/env python3
"""
This module defines a function to measure the runtime of the wait_n function.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures execution time af an async function
    args::
        n(int): number of times it is run
        max_delay(int): maximum delay between function calls
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time

    return (elapsed_time / n)
