#!/usr/bin/python3
"""
This is the "0-add_integer" module.
"""

def add_integer(a, b=98):

    """
    Adds two integers or float.

    Args:
        a (int or float): First integer.
        b (int or float): Second integer (default is 98).
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int (b)
    return a + b
