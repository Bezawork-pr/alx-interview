#!/usr/bin/python3
"""
 Given a set of consecutive integers
 starting from 1 up to and including n,
 they take turns choosing a prime number from the set
 and removing that number and its multiples
 from the set. The player that
 cannot make a move loses the game"""


def isWinner(x, nums):
    """Given a set of consecutive integers
    starting from 1 up to and including n,
    they take turns choosing a prime number from the set
    and removing that number and its multiples
    from the set. The player that
    cannot make a move loses the game"""
    player_maria_score = 0
    player_ben_score = 0
    obj = {}
    count = 0
    if x <= 0:
        return "Maria"
    for num in nums:
        obj['list_' + str(num)] = []
        for i in range(1, num + 1):
            obj['list_' + str(num)].append(i)
    for turn in range(1, x + 1):
        whose_turn = "Maria"
        num = nums[count]
        if len(obj['list_' + str(num)]) == 1:
            player_ben_score += 1
        while(len(obj['list_' + str(num)]) > 1):
            popping_mulitple = []
            for i in range(1, num + 1):
                popping_num = obj['list_' + str(num)][1]
                if i % popping_num == 0:
                    popping_mulitple.append(i)
            for i in popping_mulitple:
                obj['list_' + str(num)].remove(i)

            if len(obj['list_' + str(num)]) == 1:
                if whose_turn == "Maria":
                    player_maria_score += 1
                else:
                    player_ben_score += 1
                break
            if whose_turn == "Maria":
                whose_turn = "Ben"
            else:
                whose_turn = "Maria"
        count += 1

    if player_maria_score > player_ben_score:
        return "Maria"
    elif player_maria_score == player_ben_score:
        return None
    else:
        return "Ben"
