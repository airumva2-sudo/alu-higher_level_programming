#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve. If not
                a list of strings, all attributes are retrieved.

        Returns:
            A dict containing only the requested attributes (if attrs
            is a valid list of strings), otherwise all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str)
                                            for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
