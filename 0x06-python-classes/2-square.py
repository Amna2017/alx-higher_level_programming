#!/usr/bin/python3
"""Write an empty class Square that defines a square"""


class Square:
    """my init of class   """
    def __init__(self, size=0):
        """this is init function """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
