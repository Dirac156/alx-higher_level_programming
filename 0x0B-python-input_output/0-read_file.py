#!/usr/bin/python3
"""Read text from a file"""


def read_file(filename=""):
    """ read a file and print the output"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
