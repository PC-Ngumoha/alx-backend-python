#!/usr/bin/env python3
"""
2-measure_runtime.py

Measures the individual runtimes of each process spawn by
the wait_n() coroutine.
"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time()

    Args:
      - n: int -> number of processes to spawn
      - max_delay: int -> max value of random delay

    Return:
      - total_time / n
    """
    import time
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
