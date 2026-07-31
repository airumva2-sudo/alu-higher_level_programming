#!/usr/bin/python3
"""Defines a function that reads and prints a UTF8 text file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
