import re
import os

INIT_CHAR = 1

def is_map(data):
    return not bool(re.match(r'move', data))

def init_stacks(map_data):
    print(map_data[-1])
    max_stack = int(re.match(r'.*(\d+) *$', map_data[-1]).group(1))
    stacks = dict()

    # init empty satcks
    for num in list(range(1, max_stack+1)):
        stacks[num] = []

    reverse_data = map_data[0:-1]
    reverse_data.reverse()

    for data in reverse_data:
        print(data)
        for index in range(max_stack):
            item_index = 1 + index * 4

            if len(data) > item_index:
                item = data[item_index]
                if item != ' ':
                    stacks[index+1].append(item)

    return stacks

def export(stacks):
    for key, stack in stacks.items():
        print(f"{key}: {stack}")


def move(stacks, data):
    num, from_, to_ = [int(item) for item in re.match(r'move (\d+) from (\d+) to (\d+)', data).groups()]
    from_stack = stacks[from_]
    to_stack = stacks[to_]

    move_items = from_stack[-num:]
    to_stack += move_items[::-1]
    del from_stack[-num:]

def move_same_order(stacks, data):
    num, from_, to_ = [int(item) for item in re.match(r'move (\d+) from (\d+) to (\d+)', data).groups()]
    from_stack = stacks[from_]
    to_stack = stacks[to_]

    move_items = from_stack[-num:]
    to_stack += move_items
    del from_stack[-num:]

def quest_1(datas):
    map_data = []
    stacks = None

    for data in datas.split("\n"):
        if data == '':
            if len(map_data) > 0:
                stacks = init_stacks(map_data)
                map_data.clear()
                export(stacks)
            continue

        if is_map(data):
            map_data.append(data)
        else:
            print(data)
            move(stacks, data)
            export(stacks)

    result = ''
    for stack in stacks.values():
        result += stack[-1]

    return result

def quest_2(datas):
    map_data = []
    stacks = None

    for data in datas.split("\n"):
        if data == '':
            if len(map_data) > 0:
                stacks = init_stacks(map_data)
                map_data.clear()
                export(stacks)
            continue

        if is_map(data):
            map_data.append(data)
        else:
            print(data)
            move_same_order(stacks, data)
            export(stacks)

    result = ''
    for stack in stacks.values():
        result += stack[-1]

    return result

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    day = re.match(r'day_(\d+).py', file_name).group(1)
    inputs = open(f"{day}.txt", 'r', encoding='utf-8').read()

    print(f"{quest_1(inputs) = }")
    print(f"{quest_2(inputs) = }")
