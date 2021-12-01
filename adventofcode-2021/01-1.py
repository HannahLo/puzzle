import sys

list = open('input.txt', 'r').read().split('\n')

if list[-1] == '':
    list.pop()

greater_count = 0

pre_num = sys.maxsize
for num_str in list:
    num = int(num_str)
    if num > pre_num:
        greater_count += 1
    pre_num = num

print(greater_count)
