#!/usr/bin/python3
""" my class """


class MyInt(int):
    """ my class """
    def __eq__(self, other):
        """ my class func """
        return super().__ne__(other)

    def __ne__(self, other):
        """ my class ne func """
        return super().__eq__(other)
