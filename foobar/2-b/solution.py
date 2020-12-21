def solution(xs):
    positive = []
    negative = []
    has_zero = False

    for num in xs:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            has_zero = True

    if len(positive) == 0 and len(negative) == 0:
        return '0'
    elif len(positive) == 0 and len(negative) == 1:
        if has_zero:
            return '0'
        else:
            return str(negative[0])

    if len(negative) % 2 != 0:
        negative.sort()
        negative = negative[:len(negative)-1]

    result = 1
    for num in positive + negative:
        result *= num

    return str(result)

