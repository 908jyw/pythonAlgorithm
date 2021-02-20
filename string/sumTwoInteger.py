# [string] 두 정수 사이의 합 - 프로그래머스 1단계

def solution(a, b):
    answer = 0

    if (b < a):
        a, b = b, a
    if (a == b):
        return a

    for i in range(a, b + 1):
        answer = answer + i

    return answer