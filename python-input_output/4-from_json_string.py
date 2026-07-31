#!/usr/bin/python3
"""Defines a function that parses a JSON string into a Python object."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        The Python object represented by my_str.
    """
    return json.loads(my_str)
