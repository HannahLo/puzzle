"""
https://adventofcode.com/2021/day/9
--- Day 9: Smoke Basin ---
--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""

from sys import argv
from typing import List, Tuple

FILE = argv[1]

data = []
with open(FILE) as f:
    for line in f.read().splitlines():
        data.append([char for char in line])

MAX_WIDTH = len(data[0])
MAX_HEIGHT = len(data)

lowest_nums = []

def gen_around_pos(pos):
    return [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]-1], [pos[0], pos[1]+1]]

def valid_position(pos: tuple[int, int], range: tuple[int, int]) -> bool:
    x, y = pos
    return x >= 0 and x < range[0] and y >= 0 and y < range[1]

def is_lowest(num: int, compare: list[int]) -> bool:
    return num < min(compare)

def basin_size(pos):
    if pos not in visited_postions:
        visited_postions.append(pos)
    else:
        return 0

    poses = gen_around_pos(pos)

    size_pos = []
    for pos in poses:
        # print(f"visited position {visited_postions}")

        if not valid_position(pos, (MAX_WIDTH, MAX_HEIGHT)):
            continue
        if pos in visited_postions:
            continue

        x, y = pos
        if int(data[y][x]) < 9:
            # print(f"num: {data[y][x]} pos: {pos}")
            size_pos.append(pos)

    # print(size_pos)
    if len(size_pos) == 0:
        return 1
    else:
        total_size = 1
        for pos in size_pos:
            size = basin_size(pos)
            total_size += size
        return total_size


for i in range(MAX_WIDTH):
    for j in range(MAX_HEIGHT):
        around_poses = gen_around_pos([i,j])

        around_nums = []
        for postion in around_poses:
            if valid_position(postion, (MAX_WIDTH, MAX_HEIGHT)):
                around_nums.append(data[postion[1]][postion[0]])

        if is_lowest(data[j][i], around_nums):
            # i:x j:y
            # data: [data[j][i]
            lowest_nums.append([data[j][i], [i, j]])

"""
要從最低點算出盆地大小
應該用 recursive 的方式
"""

size_list = []
for lowest_num in lowest_nums:
    visited_postions = []
    size = basin_size(lowest_num[1])
    # print(f"num: {lowest_num[0]}, size: {size}, len: {len(visited_postions)}")
    size_list.append(size)

size_list.sort(reverse=True)
# print(size_list)

result = 1
for index in range(3):
    result *= size_list[index]

print(result)

