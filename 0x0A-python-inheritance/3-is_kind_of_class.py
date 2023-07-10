#!/usr/bin/python3
""" my class if exit or not """


def is_kind_of_class(obj, a_class):
    """ my check if enheritance or no """
    if type(obj) is a_class:
        return True
    elif isinstance(type(obj), a_class):
        return True
    else:
        return False
