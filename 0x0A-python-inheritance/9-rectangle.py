#!/usr/bin/python3
""" my class """


class BaseGeometry:
    """ my class """
    def area(self):
        """ my class func """
        raise NotImplementedError("area() method not implemented")

    def perimeter(self):
        """ my class func """
        raise NotImplementedError("perimeter() method not implemented")


class Rectangle(BaseGeometry):
    """ my class func """
    def __init__(self, width, height):
        """ my class func """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def integer_validator(self, name, value):
        """ my class func """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def area(self):
        """ my class func """
        return self.__width * self.__height

    def __str__(self):
        """ my class func """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """ my class func """
        return self.__str__()
