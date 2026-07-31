#!/usr/bin/python3
"""Defines a function that returns the dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        A dictionary representation of obj's instance attributes.
    """
    return obj.__dict__
