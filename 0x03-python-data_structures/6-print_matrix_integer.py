#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for numb in lst:
            l = len(lst) - 1
            if lst.index(numb) == l:
                print("{}".format(numb))
            else:
                print("{}".format(numb), end=' ')
