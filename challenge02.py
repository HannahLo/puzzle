def solution(total_lambs):
    return max_payout(total_lambs) - min_payout(total_lambs)

def min_payout(LAMBs):
    return (LAMBs + 1).bit_length() -1

def max_payout(LAMBs):
    from math import log, ceil, sqrt
    sqrt_five = sqrt(5)
    return int(ceil(log((LAMBs + 1 + 0.5) * sqrt_five, (1 + sqrt_five) / 2)) - 3)

print (solution(10), solution(143))
