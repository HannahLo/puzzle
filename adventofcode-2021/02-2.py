
list = open(sys.argv[1], 'r').read().split('\n')

H = 'horizontal'
D = 'depth'
A = 'aim'

data = {
    H: 0,
    D: 0,
    A: 0
}

for line in list:
    result = line.split(' ')

    if len(result) != 2:
        continue

    act = result[0]
    num = int(result[1])

    if act == 'forward':
        data[H] += num
        data[D] += data[A] * num
    elif act == 'down':
        data[A] += num
    elif act == 'up':
        data[A] -= num

print(data[H] * data[D])

# test: 900
# answer: 2086261056
