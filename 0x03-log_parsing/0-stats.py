#!/usr/bin/python3
"""
Write a script that reads stdin line by line
and computes metrics
"""
import sys

count = 1
add_file_size = 0

s_repeat = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}
for line in sys.stdin:
    log_list = line.split(" ")
    count += 1
    if count == 10:
        print("File size: {}".format(add_file_size))
        sorted_dict = sorted(s_repeat.items(), key=lambda x: x[1])
        for key, value in sorted_dict:
            print("{}: {}".format(key, value))
        count = 1
    s_repeat[log_list[-2]] += 1
    add_file_size += int(log_list[-1])
