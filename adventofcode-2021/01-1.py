import sys

list = open(sys.argv[1], 'r').read().split('\n')

if list[-1] == '':
    list.pop()

greater_count = 0

for number in range(1, len(list)):
    num = int(list[number])
    pre_num = int(list[number - 1])
    if num > pre_num:
        greater_count += 1

print(greater_count)
