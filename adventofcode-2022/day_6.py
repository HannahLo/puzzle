import re
import os

def quest_1(datas):
    NUMBER = 4
    for index in range(0, len(datas)-NUMBER-1):
        if len(set(datas[index:index+NUMBER])) == NUMBER:
            return index + NUMBER


def quest_2(datas):
    NUMBER = 14
    for index in range(0, len(datas)-NUMBER-1):
        if len(set(datas[index:index+NUMBER])) == NUMBER:
            return index + NUMBER

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
