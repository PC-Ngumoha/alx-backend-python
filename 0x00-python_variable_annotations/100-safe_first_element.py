#!/usr/bin/env python3
"""
100-safe_first_element.py

Annotation challenge
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Annotation challenge
    """
    if lst:
        return lst[0]
    else:
        return None
