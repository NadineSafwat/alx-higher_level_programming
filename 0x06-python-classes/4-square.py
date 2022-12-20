#!/usr/bin/python3
"""Define class Square."""


class Square:
    """A class defines a square"""
    def __init__(self, size=0):
        """Initialize square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the square are of the object"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value of the square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
