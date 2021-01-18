#!/usr/bin/python3
""" """


class MyInt(int):
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return (self.a != other)

    def __ne__(self, other):
        return (self.a == other)
