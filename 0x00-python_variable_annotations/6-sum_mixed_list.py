#!/usr/bin/env python3
"""
6-sum_mixed_list.py

Contains the sum_mixed_list() which accepts a list of integers
and floating point numbers and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    sum_mixed_list(mxd_list)

    Args:
      - mxd_list -> Mixed list of integers and floating points

    Returns:
      - sum(mxd_list) -> sum of mxd_list
    """
    sum = 0.0
    for num in mxd_list:
        sum += num
    return sum
