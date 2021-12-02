import sys

input = open(sys.argv[1], 'r').read().split('\n')

if input[-1] == '':
    input.pop()

greater_count = 0

"""
for idx in range(3, len(input)):
    # (int(input[idx-1]) + int(input[idx-2]) + int(input[idx-3])) < (int(input[idx]) + int(input[idx-1]) + int(input[idx-2]))
    # int(input[idx-3]) < int(input[idx-2])
    if int(input[idx-3]) < int(input[idx-2]):
        greater_count+=1
"""


# actually, check 0 -> len-4
for idx in range(0, len(input)-3):
    if int(input[idx]) < int(input[idx+1]):
        greater_count+=1

print(greater_count)
