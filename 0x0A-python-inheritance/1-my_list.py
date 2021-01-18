#!/usr/bin/python3
""" This is a function """


class MyList(list):
    """ print new list """
    def print_sorted(self):
        new = []
        for i in self:
            new.append(i)
        new.sort()
        print(new)
