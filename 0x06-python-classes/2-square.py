#!/usr/bin/python3
"""
This file contains the class Square
"""


class Square():
    """
    This is the Square class
    """
    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
