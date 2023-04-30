#!/usr/bin/python3
"""This file contains a method that can that
determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Check if all the boxes can be unlocked"""
    check_box, boxes_new, keys = [], [], boxes[0]
    start_point, flag, count = 1, 1, 0
    if (len(boxes) == 1):
        return True
    for key in keys:
        check_box.append(key)
    while flag == 1:
        for i in range(start_point, len(check_box) + 1):
            if i + 1 == len(boxes):
                flag = 0
                break
            keys = boxes[i]
            for key in keys:
                if key > len(boxes):
                    return False
                check_box.append(key)
    set_check_box = set(check_box)
    for i in boxes:
        for m in i:
            boxes_new.append(m)
    set_boxes = set(boxes_new)
    if len(set_check_box) != len(set_boxes):
        return False
    return True
