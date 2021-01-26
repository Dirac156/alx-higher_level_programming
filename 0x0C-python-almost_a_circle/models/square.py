#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ class Square innerite from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """construct square method"""
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """ size property """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """overide parent's str method"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)
