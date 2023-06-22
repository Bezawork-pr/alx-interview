#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    param = 0
    count_row = 0
    for row in grid:
        for cell in range(len(row)):
            if row[cell] == 1:
                param += 4
            if row[cell] == 1 and cell != 0 and cell != len(row) - 1:
                if row[cell - 1] == 1:
                    param -= 1
                if row[cell + 1] == 1:
                    param -= 1
            if row[cell] == 1 and count_row != 0 and count_row != len(row) - 1:
                if grid[count_row - 1][cell] == 1:
                    param -= 1
                if grid[count_row + 1][cell] == 1:
                    param -= 1
        count_row += 1
    return param
