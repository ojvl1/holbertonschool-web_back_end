#!/usr/bin/env python3
""" Function element_length that takes a list
    lst of strings as argument and returns a list
    of integers representing the lengths of the
    corresponding strings
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuples """
    return [(i, len(i)) for i in lst]
