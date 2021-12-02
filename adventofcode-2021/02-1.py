import sys

list = open(sys.argv[1], 'r').read().split('\n')

H = 'horizontal'
D = 'depth'

data = {
    H: 0,
    D: 0
}

for line in list:
    result = line.split(' ')

    if len(result) != 2:
        continue

    act = result[0]
    num = int(result[1])

    if act == 'forward':
        data[H] += num
    elif act == 'down':
        data[D] += num
    elif act == 'up':
        data[D] -= num

print(data[H] * data[D])

# test: 150
# answer: 6
