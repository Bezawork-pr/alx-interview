#!/usr/bin/python3
from math import factorial
def pascal_triangle(n):
    my_list = []
    if n <= 0:
        return my_list
    for row in range(n):
        new_list = [1]
        for column in range(row):
            if column == row - 1:
                my_append = 1
            elif row % 2 != 0 and column == 0:
                my_append = row * (column + 1)
            elif row % 2 == 0 and column == 0:
                my_append = row * (column + 1)
            elif row % 2 == 0 and column == 1:
                my_append = (row - 1) * 2
            elif row % 2 != 0 and column == 1 and row > 3:
                my_append = row * (column + 1)
            elif row % 2 == 0 and (row - column) == 2:
                my_append = row
            else:
                pass
            new_list.append(my_append)
        my_list.append(new_list)
        del new_list
    return my_list
