#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function that return a tuple"""
    return (k), (v**2)
