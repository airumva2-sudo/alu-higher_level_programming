#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or one of its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)
