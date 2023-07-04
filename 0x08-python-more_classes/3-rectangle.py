#!/usr/bin/python3
""" my new class """


class Rectangle:
    """ my new class """
    def __init__(self, width=0, height=0):
        """ my new class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ my new class """
        return self.__width

    @width.setter
    def width(self, value):
        """ my new class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ my new class """
        return self.__height

    @height.setter
    def height(self, value):
        """ my new class """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ my new class """
        return self.width * self.height

    def perimeter(self):
        """ my new class """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ my new class """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.strip()
