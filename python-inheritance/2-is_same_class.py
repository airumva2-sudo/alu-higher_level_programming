#!/usr/bin/python3
"""Defines a function that checks an object's exact class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj's type is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
