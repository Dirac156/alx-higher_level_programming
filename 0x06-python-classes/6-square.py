#!/usr/bin/python3
"""
This file contains the class Square
"""


class Square():
    """
    This is the Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
        if isinstance(position, tuple) is not True or len(position) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif type(position[0]) != int or type(position[1]) != int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for numb in range(0, self.__position[1]):
                print("")
            for el in range(0, self.__size):
                for numb in range(0, self.__position[0]):
                    print(" ", end="")
                for el_2 in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is not True or len(value) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif isinstance(value[0], int) is not True or type(value[1]) != int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif value[0] < 0 or value[1] < 0:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = value
