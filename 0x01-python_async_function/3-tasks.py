#!/usr/bin/env python3
"""
This module defines a function to measure the runtime of the wait_n function.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    args::
        max_delay(int)
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
