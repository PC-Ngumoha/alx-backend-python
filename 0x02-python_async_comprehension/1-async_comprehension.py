#!/usr/bin/env python3
"""
0-async_comprehension.py

Contains the definition of the coroutine 'async_comprehension'
which returns a list of random numbers gotten from a generator
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension

    Return:
      - List[float] -> list of random floating point numbers
    """
    output = [num async for num in async_generator()]
    return output
