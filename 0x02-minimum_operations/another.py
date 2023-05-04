#!/usr/bin/python3
"""Given a number n, write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file"""


def minOperations(n):
    """Return the minimum amount of operation needed
    to reach n amount of H"""
    num, num_of_operations, cp_paste_operation = 1, 0, 2
    paste_operation, flag, i, count = 1, 1, 0, 0
    increment = [1, 3, 6, 12]
    if n <= 0:
        return 0
    while(num != n and num < n):
        count += 1
        if count == 50:
            return 0
        if flag == 1 and n - num > increment[i]:
            flag = 0
            if num_of_operations == 0:
                num_of_operations = cp_paste_operation
                num = num + increment[i]
            else:
                num_of_operations = num_of_operations + cp_paste_operation
                print(num_of_operations)
                if (n - num > i):
                    i = i + 1
                num = num + increment[i]
        elif flag == 0:
            print('What is going on bug')
        else:
            print('Do u get here')
            num = num + increment[i]
            num_of_operations = num_of_operations + paste_operation
            print(num_of_operations)
            flag = 1
        return num_of_operations

