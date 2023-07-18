#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    visit = set()

    def dfs(row, column):
        """Find Island and calculate"""
        if row >= len(grid) or column >= len(grid[0]) or \
                row < 0 or column < 0 or grid[row][column] == 0:
            return 1
        if (row, column) in visit:
            return 0

        visit.add((row, column))
        perimeter = dfs(row, column + 1)
        perimeter += dfs(row + 1, column)
        perimeter += dfs(row, column - 1)
        perimeter += dfs(row - 1, column)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
