#!/usr/bin/python3
"""
Write a script that reads stdin line by line
and computes metrics
debug checker error
"""

if __name__ == "__main__":
    import sys

    def printer(add_file_size, s_repeat):
        print("File size: {}".format(add_file_size))
        sorted_dict = sorted(s_repeat.items())
        for key, value in sorted_dict:
            if s_repeat[key] != 0:
                print("{}: {}".format(key, value))

    total = 0
    current = 10
    add_file_size = 0

    s_repeat = {"200": 0, "301": 0, "400": 0, "401": 0,
           "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            log_list = line.split(" ")
            print(log_list)
            dict_values = list(s_repeat.values())
            total = sum(dict_values)
            if total == current:
                printer(add_file_size, s_repeat)
                current += 10
            else:
                total = 0
            s_repeat[log_list[-2]] += 1
            add_file_size += int(log_list[-1])
    except KeyboardInterrupt:
        printer(add_file_size, s_repeat)
        raise
