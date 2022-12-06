import re
import os

def score(char):
    if char.isupper():
        return 27 + ord(char) - ord('A')
    else:
        return 1 + ord(char) - ord('a')

def quest_1(datas):
    total = 0

    for data in datas.split("\n"):
        center = len(data)//2
        pack_1 = set(data[:center])
        pack_2 = set(data[center:])

        common_item = pack_1 & pack_2

        for item in common_item:
            total += score(item)

    return total

def quest_2(datas):
    total = 0
    group = []
    for data in datas.split("\n"):
        group.append(data)

        if len(group) == 3:
            common_item = set(group[0]) & set(group[1]) & set(group[2])
            for item in common_item:
                total += score(item)
            group.clear()

    return total

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
