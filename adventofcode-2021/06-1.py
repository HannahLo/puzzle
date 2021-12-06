import sys

FILE = sys.argv[1]
DAY = int(sys.argv[2])

inputs = [int(num) for num in open(FILE, 'r').read().split(',')]

# print("Initial state:", ','.join([str(i) for i in inputs]))

fishes = inputs.copy()

def handle_fish(fishes):
    new_fishes = [8]*fishes.count(0)
    new_fishes = [6 if f == 0 else f-1 for f in fishes] + new_fishes
    return new_fishes

for day in range(DAY):
    fishes = handle_fish(fishes)
    # print("After", day+1, "day:", ','.join([str(i) for i in fishes]))

print(len(fishes))
