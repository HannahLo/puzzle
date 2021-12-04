import sys

inputs = open(sys.argv[1], 'r').read().split('\n')

lucky_numbers = [int(num) for num in inputs[0].split(',')]
squares = []
tmp_square = []
wins = []

for i in range(2, len(inputs)):
    if inputs[i] == '':
        squares.append(tmp_square)
        tmp_square = []
    else:
        row = [int(num) for num in filter(None, inputs[i].split(' '))]
        tmp_square.append(row)

mark_list = [list() for _ in range(len(squares))]

def mark_square(square, lucky_number):
    # print(lucky_number)
    # print(square)
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j] == lucky_number:
                # print(i, j)
                return [i, j]
    return None

LENGTH = len(squares[0][0])

def is_bingo(marked_list):
    if len(marked_list) < LENGTH:
        return False

    # has horizontal line
    for y in range(LENGTH):
        if LENGTH == sum(1 for mark in marked_list if mark[1] == y):
            print('bingo')
            return True

    # has vertical line
    for x in range(LENGTH):
        if LENGTH == sum(1 for mark in marked_list if mark[0] == x):
            print('bingo')
            return True

    return False


def call_lucky_num():
    for number in lucky_numbers:
        for square_num in range(len(squares)):
            if square_num in [win[0] for win in wins]:
                continue

            mark = mark_square(squares[square_num], number)

            if mark != None:
                mark_list[square_num].append(mark)
                if is_bingo(mark_list[square_num]):
                    # print("number:", square_num)
                    # print("lucky number:", number)
                    # print(mark_list)
                    wins.append([square_num, number])

call_lucky_num()

last_win = wins[-1]
square_num = last_win[0]

lucky_number = last_win[1]
square = squares[square_num]
marks = mark_list[square_num]

def cal_score(lucky_number, square, marks):
    sum = 0
    for i in range(len(square)):
        for j in range(len(square[i])):
            if not [i, j] in marks:
                sum += square[i][j]
    return lucky_number*sum

print(cal_score(lucky_number, square, marks))
