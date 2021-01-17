#!/usr/bin/python3
"""
This file contains the class Rectangle
"""


class Rectangle():
    """
    This is the class rectangle
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            print("width must be an integer", end="")
            raise TypeError
        elif width < 0:
            print("width must be >= 0", end="")
            raise ValueError
        else:
            self.__width = width

        if type(height) != int:
            print("height must be an integer", end="")
            raise TypeError
        elif height < 0:
            print("height must be >= 0", end="")
            raise ValueError
        else:
            self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")