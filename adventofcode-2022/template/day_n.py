import re
import os

def quest_1(datas):
    for data in datas.split("\n"):
        pass

    return None

def quest_2(datas):
    for data in datas.split("\n"):
        pass

    return None

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
