#!/usr/bin/python3
"""write a method that calculates the fewest number
of operations needed to result in exactly
n H characters in the file"""


def minOperations(n):
    """Calculate how many operation is needed to get to n
    number of Hs"""
    num = 1
    num_of_operations = 0
    cp_paste_operation = 2
    paste_operation = 1
    flag = 1
    i = 0
    count = 0
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
