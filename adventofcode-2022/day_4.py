import re
import os

def quest_1(datas):
    max_value = 0
    value = 0

    for data in datas.split("\n"):
        if data == "":
            max_value = max(value, max_value)
            value = 0
        else:
            value += int(data)

    return max_value

def quest_2(datas):
    values = []
    value = 0

    for data in datas.split("\n"):
        if data == "":
            values.append(value)
            value = 0
        else:
            value += int(data)

    return sum(sorted(values, reverse=True)[:3])

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
