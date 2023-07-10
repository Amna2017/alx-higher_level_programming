#!/usr/bin/python3
""" my class """


class MyInt(int):
    """ my class inher """
    def __eq__(self, other):
        """ my eq func """
        return super().__ne__(other)

    def __ne__(self, other):
        """ my ne func """
        return super().__eq__(other)
