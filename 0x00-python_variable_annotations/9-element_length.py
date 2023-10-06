#!/usr/bin/env python3
"""
9-element_length.py

Annotation challenge
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotation challenge
    """
    return [(i, len(i)) for i in lst]
