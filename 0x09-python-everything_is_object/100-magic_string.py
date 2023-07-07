#!/usr/bin/python3
"""my magic """

def magic_string():
    """ function """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.count - 1)
