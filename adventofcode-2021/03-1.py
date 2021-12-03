import sys

list = open(sys.argv[1], 'r').read().split('\n')

if list[-1] == '':
    list.pop()

count = [0] * len(list[0])

for binary in list:
    for idx,digit in enumerate(binary):
        if digit == '1':
            count[idx] += 1

common_string = ''
mid_count = len(list)/2

for num in count:
    if num > mid_count:
        common_string += '1'
    else:
        common_string += '0'

bit_mask = ''.join(['1']*len(common_string))

gamma_rate = int(common_string, 2)
epsilon_rate = gamma_rate^int(bit_mask, 2)
power_consumption = gamma_rate * epsilon_rate

print(power_consumption)

# test: 198
# answer: 1234
