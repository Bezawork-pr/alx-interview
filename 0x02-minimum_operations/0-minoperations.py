#!/usr/bin/python3
"""write a method that calculates the fewest number
of operations needed to result in exactly
n H characters in the file"""
from typing import List


def minOperations(n: int) -> int:
    """Calculate how many operation is needed to get to n
    number of Hs"""
    num: int = 1
    num_of_operations: int = 0
    cp_paste_operation: int = 2
    paste_operation: int = 1
    flag: int = 1
    i: int = 0
    count: int = 0
    increment: List = [1, 3, 6, 12]
    if (type(n) != int):
        raise TypeError('Expected int')
    if n == 0:
        return 0
    while(num != n and num < n):
        count += 1
        if count == 50:
            return 0
        if flag == 1 and n - num > increment[i]:
            if num_of_operations == 0:
                num_of_operations = cp_paste_operation
                num = num + increment[i]
            else:
                num_of_operations = num_of_operations + cp_paste_operation
                if (n - num > i):
                    i = i + 1
                num = num + increment[i]
            flag = 0
        else:
            num = num + increment[i]
            num_of_operations = num_of_operations + paste_operation
            flag = 1
    return num_of_operations
