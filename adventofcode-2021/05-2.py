from sys import argv
import math
import re

inputs = open(argv[1], 'r').read().split('\n')

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

def add_count(x,y):
    point = "%d,%d" % (x,y)

    print(point)

    count = counts.get(point, 0) + 1
    counts[point] = count

for pair in pairs:
    point1 = pair[0]
    point2 = pair[1]

    if point1[0] != point2[0] and point1[1] != point2[1]:
        print(point1,'->', point2)
        distance = [point2[0]-point1[0], point2[1]-point1[1]]
        direction = [distance[0] / abs(distance[0]), distance[1] / abs(distance[1])]
        print(direction)
        for number in range(abs(distance[0])+1):
            add_count(point1[0]+number*direction[0], point1[1]+number*direction[1])
    elif point1[0] != point2[0]:
        range_list = range(point2[0], point1[0] + 1) if point1[0] > point2[0] else range(point1[0], point2[0] + 1)
        for x in range_list:
            add_count(x, point1[1])
    elif point1[1] != point2[1]:
        range_list = range(point2[1], point1[1] + 1) if point1[1] > point2[1] else range(point1[1], point2[1] + 1)
        for y in range_list:
            add_count(point1[0],y)

def cout_cross_dot(counts):
    cross_count = 0
    for count in list(counts.values()):
        if count > 1:
            cross_count += 1
    return cross_count

# print(counts)
print(cout_cross_dot(counts))
