#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new = []
        for i in self:
            new.append(i)
        new.sort()
        print(new)