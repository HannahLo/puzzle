

import sys

FILE = sys.argv[1]
DAY = int(sys.argv[2])

inputs = [int(num) for num in open(FILE, 'r').read().split(',')]

count = [0]*9
for num in inputs:
    count[num] += 1

def handle_fish():
    zero_num = count[0]

    for i in range(1,9):
        count[i-1] = count[i]

    count[8] = zero_num
    count[6] += zero_num

for day in range(DAY):
    handle_fish()

print(sum(count))
