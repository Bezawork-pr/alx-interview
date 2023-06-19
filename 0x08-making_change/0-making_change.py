#!/usr/bin/python3
"""Determine the fewest number of coins
needed to meet a given amount total"""


def makeChange(coins, total):
    """Determine the fewest number
    of coins needed to meet
    a given amount total"""
    if total == 0 or total < 0:
        return 0
    if len(coins) == 0:
        return -1
    num_of_coins = 0
    while (total > 0):
        largest = coins[0]
        for i in range(len(coins)):
            if coins[i] > largest and coins[i] <= total:
                largest = coins[i]
            if coins[i] > total or i == len(coins) - 1:
                total -= largest
                num_of_coins += 1
                break
    if total == 0:
        return num_of_coins
    return -1
