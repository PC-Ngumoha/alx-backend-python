#!/usr/bin/env python3
"""
8-make_multiplier.py

Contains the factory function make_multiplier() that takes a float
and returns a function that multplies a given value by that float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier(multiplier)

    Args:
      - multiplier -> floating point parameter

    Returns:
      - func(multiplier) -> function
    """
    return lambda value: value * multiplier
