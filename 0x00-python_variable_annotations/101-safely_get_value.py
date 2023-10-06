#!/usr/bin/env python3
"""
101-safely_get_value.py

Annotation challenge
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
      ) -> Union[Any, T]:
    """
    Annotation challenge
    """
    if key in dct:
        return dct[key]
    else:
        return default
