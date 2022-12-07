import re
import os

def quest_1(datas):
    value = 0

    for data in datas.split("\n"):
        if data == '':
            continue

        a_start, a_end, b_start, b_end = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', data).groups()
        a = set(range(int(a_start), int(a_end) + 1))
        b = set(range(int(b_start), int(b_end) + 1))
        common_length = len(a & b)
        if common_length == len(a) or common_length == len(b):
            value += 1

    return value

def quest_2(datas):
    value = 0

    for data in datas.split("\n"):
        if data == '':
            continue

        a_start, a_end, b_start, b_end = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', data).groups()
        a = set(range(int(a_start), int(a_end) + 1))
        b = set(range(int(b_start), int(b_end) + 1))
        common_length = len(a & b)
        if common_length > 0:
            value += 1

    return value

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
