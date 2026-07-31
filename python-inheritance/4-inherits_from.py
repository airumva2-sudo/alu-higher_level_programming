#!/usr/bin/python3
"""Defines a function that checks if an object's class inherited from another class."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj's class is a subclass of a_class (but not a_class
        itself), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
