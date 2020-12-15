#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for numb in new_list:
        print("{:d}".format(numb))
    return my_list
