#!/usr/bin/python3
"""Solve nqueen problem by using recursion to backtrack
Rules attack diagonally, horizontally and vertical. Therefore
no two queens should be in the attack zone"""
import argparse
def error_message():
    print("Usage: nqueens N")
    exit(1)
parser = argparse.ArgumentParser()
parser.error = error_message()
parser.add_argument("N")
args = parser.parse_args()
n = int(args.a)
def nqueen(n):
    col = set()
    positive_diagonal = set()
    negative_diagonal = set()
    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                continue
            col.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            col.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return result
nqueen = nqueen(n)
val = "Q"
for sol in nqueen:
    my_result = [[index, row.index(val)] for index, row in enumerate(sol) if val in row]
    print(my_result)
