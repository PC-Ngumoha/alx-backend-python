#!/usr/bin/env python3
"""
7-to_kv.py

Contains the function to_kv() which accepts a string and float | int
and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv(k, v)

    Args:
      - k -> string parameter
      - v -> int | float parameter

    Return:
      - (k, v**2) -> tuple containing k and the square of v
    """
    return (k, v**2)
