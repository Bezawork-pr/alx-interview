#!/usr/bin/python3
"""Given an n x n 2D matrix,
rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix
    rotate it 90 degrees clockwise"""
    length = len(matrix)
    new_matrix = []
    count = 0
    for i in range(length):
        new_matrix.append([])
    for row in matrix:
        count = 0
        for column in row:
            new_matrix[count].insert(0, column)
            count += 1
    count = 0
    for row in matrix:
        for column in range(len(row)):
            row[column] = new_matrix[count][column]
        count += 1
