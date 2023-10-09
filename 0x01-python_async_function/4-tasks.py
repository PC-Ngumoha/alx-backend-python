#!/usr/bin/env python3
"""
4-tasks.py

expansion of 3-tasks.py which actually does something
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n()

    Args:
      - n -> number of times to spawn async requests
      - max_delay -> max delay value

    Return:
      - list of floats
    """
    output = await asyncio.gather(
        *[task_wait_random(max_delay) for i in range(n)]
    )
    return sorted(output)
