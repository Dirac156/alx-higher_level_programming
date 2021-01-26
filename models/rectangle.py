#!/usr/bin/python3
""" This is a rectangle file"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""

    def __init__(self, width, heigth, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.__width = width
        self.__heigth = heigth
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        elif value <= 0:
            raise ValueError("heigth must be > 0")
        else:
            self.__heigth = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y= value

    def __str__(self):
        return (f"{self.__width}, {self.__heigth}, {self.__x}, {self.__y}")