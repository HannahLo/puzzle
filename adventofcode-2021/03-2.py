import sys

list = open(sys.argv[1], 'r').read().split('\n')

if list[-1] == '':
    list.pop()

digit_size = len(list[0])

def get_digit(list, index, mode):
    # print("lsit:", list)
    # print("index:", index)

    count = 0
    zero_list = []
    one_list = []
    for binary in list:
        digit = binary[index]
        if digit == '1':
            count += 1
            one_list.append(binary)
        else:
            zero_list.append(binary)

    current_digit = ''
    if mode == 'most':
        current_digit = '1' if count*2 >= len(list) else '0'
    else:
        current_digit = '1' if count*2 < len(list) else '0'

    # print("current_digit:", current_digit)

    sub_list = one_list if current_digit == '1' else zero_list

    next_index = index+1
    if len(sub_list) == 1:
        return current_digit + sub_list[0][next_index:]
    elif next_index < digit_size:
        return current_digit + get_digit(sub_list, index+1, mode)
    else:
        return current_digit

most_digit = get_digit(list, 0, 'most')
less_digit = get_digit(list, 0, 'less')

# print("most_digit:", most_digit, "less:", less_digit)

oxygen_rate = int(most_digit, 2)
co2_rate = int(less_digit, 2)
power_consumption = oxygen_rate * co2_rate

print(power_consumption)
