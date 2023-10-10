#!/usr/bin/env python3
"""
2-measure_runtime.py

Creates a coroutine which measures the runtime for executing
another coroutine four times in parallel
"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime()

    Return:
      - runtime -> floating point number representing the total runtime
    """
    import time
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return time.perf_counter() - start_time
