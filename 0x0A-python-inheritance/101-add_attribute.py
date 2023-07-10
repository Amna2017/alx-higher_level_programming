#!/usr/bin/python3
""" my class """


def add_attribute(obj, attr, value):
    """ my class func """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr] = value
