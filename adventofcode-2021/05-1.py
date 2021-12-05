import sys

import re

inputs = open(sys.argv[1], 'r').read().split('\n')

pairs = []
counts = {}

for line in inputs:
    if line == '':
        continue

    regex = re.compile(r'(\d*),(\d*) -> (\d*),(\d*)')
    match = regex.match(line)
    point1 = [int(match.group(1)), int(match.group(2))]
    point2 = [int(match.group(3)), int(match.group(4))]
    pairs.append([point1, point2])


for pair in pairs:
    point1 = pair[0]
    point2 = pair[1]

    if point1[0] != point2[0] and point1[1] != point2[1]:
        continue
    elif point1[0] != point2[0]:
        range_list = range(point2[0], point1[0] + 1) if point1[0] > point2[0] else range(point1[0], point2[0] + 1)
        for x in range_list:
            point = f'{x},{point1[1]}'
            count = counts.get(point, 0) + 1
            counts[point] = count
            # print(f'point: {point} count: {count}')
    elif point1[1] != point2[1]:
        range_list = range(point2[1], point1[1] + 1) if point1[1] > point2[1] else range(point1[1], point2[1] + 1)
        for y in range_list:
            point = f'{point1[0]},{y}'
            count = counts.get(point, 0) + 1
            counts[point] = count
            # print(f'point: {point} count: {count}')

def cout_cross_dot(counts):
    cross_count = 0
    for count in list(counts.values()):
        if count > 1:
            cross_count += 1
    return cross_count

# print(counts)
print(cout_cross_dot(counts))
