#!/usr/bin/env python3
"""
0-async_generator.py

Contains the definition of the coroutine 'async_generator' which loops
ten times and returns a random number between 1 and 10 each time it's
called.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator()

    Yields:
      - a number between 1 and 10 each time it's called
    """
    for i in range(10):
        yield random.uniform(1, 10)
        await asyncio.sleep(1.0)
