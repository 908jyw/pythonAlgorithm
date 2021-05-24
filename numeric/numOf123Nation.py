# [Numeric] 124 나라의 숫자 - 프로그래머스

import itertools


def solution(n):
    answer = ''

    #     x = 0
    #     i = 0
    #     while True:
    #         x += 1
    #         i += 1
    #         x = 3 * x
    #         if(n <= x):
    #             break

    #     result = list(map(''.join,itertools.product('124',repeat=i)))

    #     answer = result[n - (x//3 - 1) -1]

    # n = 15

    # if(0<n<4):
    #     yn = False
    # else:
    #     yn = True

    while True:
        # print(n)
        if (0 < n < 3):
            answer = str(n % 3) + answer
            break
        else:
            answer = '124'[(n - 1) % 3] + answer
            n = (n - 1) // 3
            if (n == 0):
                break

    print(answer)

    return answer

n = 499999999

print(solution(n))