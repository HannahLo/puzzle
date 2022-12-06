#!/usr/bin/python

import re
import os

'''
A X Rock
B Y Paper
C Z Scissor
'''

def score_1(strategy):
    MAP = {
        'A X': 1+3,
        'A Y': 2+6,
        'A Z': 3+0,
        'B X': 1+0,
        'B Y': 2+3,
        'B Z': 3+6,
        'C X': 1+6,
        'C Y': 2+0,
        'C Z': 3+3
    }
    return MAP[strategy]

def score_2(strategy):
    '''
    X lose
    Y even
    Z win
    '''
    MAP = {
        'A X': 0+3, # Z
        'A Y': 3+1, # X
        'A Z': 6+2, # Y
        'B X': 0+1, # X
        'B Y': 3+2, # Y
        'B Z': 6+3, # Z
        'C X': 0+2, # Y
        'C Y': 3+3, # Z
        'C Z': 6+1  # X
    }
    return MAP[strategy]

def quest_1(datas):
    total = 0

    for data in datas.split("\n"):
        if len(data) == 0:
            continue

        total += score_1(data)

    return total

def quest_2(datas):
    total = 0

    for data in datas.split("\n"):
        if len(data) == 0:
            continue

        total += score_2(data)

    return total

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
