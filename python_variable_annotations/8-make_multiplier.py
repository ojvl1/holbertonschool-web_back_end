#!/usr/bin/env python3
""" Complex types - functions """
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Function that return a function
        that multiplies a float
    """

    def multiply(n: float) -> float:
        """
        Return the result of a float and multiplier
        """
        return n * multiplier
    return multiply
