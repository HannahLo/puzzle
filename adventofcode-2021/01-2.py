import sys

input = open(sys.argv[1], 'r').read().split('\n')

if input[-1] == '':
    input.pop()

def get_grater_count(list):
    greater_count = 0

    pre_num = sys.maxsize
    for num_str in list:
        num = int(num_str)
        if num > pre_num:
            greater_count += 1
        pre_num = num

    return greater_count


sum_list = []

for idx, val in enumerate(input):
    if idx > 1:
        sum = int(input[idx]) + int(input[idx-1]) + int(input[idx-2])
        sum_list.append(sum)

print(get_grater_count(sum_list))
