import sys

FILE = sys.argv[1]

only_digit_lens = [2,3,4,7]
input_values = []
output_values = []

def grep_digits(line):
    return [''.join(sorted(digit)) for digit in line.split(' ')]

for line in open(FILE, 'r').read().split('\n'):
    if line == '':
        continue

    inputs, outputs = line.split(' | ')
    input_values += grep_digits(inputs)
    output_values += grep_digits(outputs)

only_digit_count = 0

for digit in output_values:
    digit_len = len(digit)
    if digit_len in only_digit_lens:
        only_digit_count += 1

print(only_digit_count)
