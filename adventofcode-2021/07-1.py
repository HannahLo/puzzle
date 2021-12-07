import sys

FILE = sys.argv[1]

inputs = [int(num) for num in open(FILE, 'r').read().split(',')]

dic = {}

for num in inputs:
    dic[num] = dic.get(num, 0) + 1

total_sum = sum([num*count for num, count in dic.items()])

num_fuel = {}


def get_fuel(center_num):
    result = 0
    for num, count in dic.items():
        result += abs(num - center_num)*count
    return result

for num in inputs:
    num_fuel[num] = get_fuel(num)

print(min(num_fuel.values()))
