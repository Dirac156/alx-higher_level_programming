#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [] or matrix == None:
        return
    else:
        new_matrix = []
        for column in matrix:
            new_column = list(map(lambda x : x*2, column))
            new_matrix.append(new_column)
        return new_matrix

print(square_matrix_simple([[2, 4], [5, 6], [10, 20]]))
print(square_matrix_simple([]))
print(square_matrix_simple(None))
