#!/usr/bin/python3
"""Defines a function that lists an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the attributes and methods of obj.
    """
    return dir(obj)
