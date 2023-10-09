#!/usr/bin/env python3
"""
Creates the function task_wait_random() which returns a new
asyncio task based on the wait_random() coroutine defined earlier
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    task_wait_random()

    Args:
      - max_delay: int -> maximum delay possible

    Returns:
      - new asyncio.Task()
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
