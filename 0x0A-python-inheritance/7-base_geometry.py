#!/usr/bin/python3
""" my class """


class BaseGeometry:
    """my class """
    pass

    def area(self):
        """my class area func """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """my class func """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

