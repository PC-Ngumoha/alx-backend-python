#!/usr/bin/env python3
"""
0-basic_async_syntax.py

Contains the definition of the wait_random() function which
displays how to use asyncio package to work with asynchronous
code in python.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random()

    Args:
      - max_delay -> int parameter

    Return:
      - output -> random float output between 0 and max_delay
    """
    output = random.uniform(0, max_delay)
    await asyncio.sleep(output)
    return output
