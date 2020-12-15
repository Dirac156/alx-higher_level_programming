#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for lst in matrix:
        for numb in lst:
            l = len(lst) - 1
            if lst.index(numb) == l:
                print("{:d}".format(numb))
            else:
                print("{:d}".format(numb), end=' ')
