#!/usr/bin/python3
"""function that returns the dictionary
description with simple data structure"""


def class_to_json(obj):
    """creates a json representation of an object without using
        json module. One liner!! (without pep8 fix) :D
    """
    return repr({key: value for key, value in obj.__dict__.items()})
