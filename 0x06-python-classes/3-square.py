#!/usr/bin/python3
"""This module has a class square
   and a method that returns the area of the class"""


class Square:
    """This class has private instance for the size
        and also a public method for the area"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
