#!/usr/bin/python3
"""write a method that calculates the fewest number
of operations needed to result in exactly
n H characters in the file"""
def minOperations(n):
    num = 1
    number_of_operations = 0
    copy_paste_operation = 2
    paste_operation = 1
    flag = 1
    i = 0
    count = 0
    increment = [1, 3, 6, 12]
    while(num != n and num < n):
        count += 1
        if count == 50:
            return 0
        print(num, n)
        if flag == 1:
            if number_of_operations == 0:
                number_of_operations = copy_paste_operation
                num = num + increment[i]
            else:
                number_of_operations = number_of_operations + copy_paste_operation
                if (n - num > i):
                    print("Do u get here")
                    i = i + 1
                num = num + increment[i]
            flag = 0
        else:
            num = num + increment[i]
            number_of_operations = number_of_operations + 1
            flag = 1
    return number_of_operations
