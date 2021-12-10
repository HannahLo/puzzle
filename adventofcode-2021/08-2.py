# Seven-segment display
# https://en.wikipedia.org/wiki/Seven-segment_display
# https://observablehq.com/@visnup/day-8-seven-segment-search

import sys

FILE = sys.argv[1]

digit_number_pair = {}
only_digit_lens = [2,3,4,7]
input_values = []
output_values = []

def grep_digits(line):
    return list(line.split(' '))

for line in open(FILE, 'r').read().split('\n'):
    if line == '':
        continue

    inputs, outputs = line.split(' | ')
    input_values += grep_digits(inputs)
    output_values += grep_digits(outputs)
