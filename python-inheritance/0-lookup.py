#!/usr/bin/python3
"""Defines a function that returns the list of attributes/methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the attributes and methods of obj.
    """
    return dir(obj)
