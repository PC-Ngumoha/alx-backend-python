#!/usr/bin/env python3
"""
5-sum_list.py

Contains the definition of the function sum_list which accepts
a list of floating point numbers and returns their running total
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list(input_list)

    Args:
      - input_list -> list of floating point numbers

    Return:
      - total(input_list) -> running total derived from list
    """
    total = 0.0
    for num in input_list:
        total += num
    return total
