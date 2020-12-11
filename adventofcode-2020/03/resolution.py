import os
dir_path = os.path.dirname(os.path.realpath(__file__))

file_path = dir_path + '/data.txt'
# file_path = dir_path + '/test-data.txt'

data_ary = []

with open(file_path) as data_file:
    for line in data_file:
        data_ary.append(list(line.rstrip()))

height = len(data_ary)
width = len(data_ary[0])

print("height: " + str(height) + " width: " + str(width))

digit = '#'

def count(x, y):
    times = 0
    if y == 1:
        loop = height
    else:
        loop = (height / y) + 1
    for n in range(0, loop):
        down = n * y
        right = (x * n) % width
        # print("down: " + str(down) + " right: " + str(right))
        if data_ary[down][right] == digit:
            times += 1
    return times

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

rules = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

result = 1
for rule in rules:
    temp = count(rule[0], rule[1])
    print(temp)
    result *= temp

print("result: " + str(result))
