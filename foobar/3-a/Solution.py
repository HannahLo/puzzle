def solution(l):
    record = [0] * len(l)
    count = 0
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                record[j] += 1
                count += record[i]

    return count

# test case
print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 3, 4, 5, 7, 11]))
print(solution([1]))
print(solution([1,1]))
