#!/usr/bin/python3
"""
This file contains a function
that determines if a given
data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Determine if a given data set
    represents a valid UTF-8 encoding"""
    data_binary_list = []
    for i in range(len(data)):
        if data[i] > 255:
            return False
        data_converted = format(data[i], 'b')
        data_binary_list.append(data_converted)
    coming_bytes = 0
    flag = 0
    for i in range(len(data_binary_list)):
        for m in data_binary_list[i]:
            if flag == 0:
                if m == '1':
                    coming_bytes += 1
                else:
                    flag = 1
                    break
            elif coming_bytes == 1 and flag == 1:
                if m == '1':
                    flag = 0
            else:
                if m == '1':
                    coming_bytes -= 1
                    break
                else:
                    break

    if coming_bytes - 1 == 0:
        return True
    return False
