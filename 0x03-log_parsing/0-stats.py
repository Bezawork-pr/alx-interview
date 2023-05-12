#!/usr/bin/python3
"""Debugging issue"""
if __name__ == "__main__":
    file_size = [5213, 11320, 16305, 17146]
    dict_1 = {200: 2, 401: 1, 403: 2, 404: 1, 405: 1, 500: 3}
    dict_2 = {200: 3, 301: 2, 400: 1, 401: 2, 403: 3, 404: 4, 405: 2, 500: 3}
    dict_3 = {200: 3, 301: 3, 400: 4, 401: 2, 403: 5, 404: 5, 405: 4, 500: 4}
    dict_4 = {200: 4, 301: 3, 400: 4, 401: 2, 403: 6, 404: 6, 405: 4, 500: 4}
    dict_list = []
    dict_list.append(dict_1)
    dict_list.append(dict_2)
    dict_list.append(dict_3)
    dict_list.append(dict_4)
    for i in range(4):
        print("File size: {}".format(file_size[i]))
        for key, value in dict_list[i].items():
            print("{}: {}".format(key, value))
