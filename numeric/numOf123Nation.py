# [Numeric] 124 나라의 숫자 - 프로그래머스

import itertools


def solution(n):
    answer = ''

    n = 39

    x = 1
    while True:
        sum = 1
        for i in range(1, x + 1):
            sum = sum * 3
        if (n <= sum):
            break
        else:
            n = n - sum
            x += 1

    result = list(map(''.join, itertools.product('124', repeat=x)))

    answer = result[n - 1]

    print(answer)

    return answer

n = 499999999

print(solution(n))