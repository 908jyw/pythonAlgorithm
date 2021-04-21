# [String] 정수 제곱근 판별 - 프로그래머스 1단계


import math
def solution(n):
    answer = 0
    answer = math.sqrt(n)
    result = answer - int(answer)
    if(result > 0):
        return -1
    else:
        answer = (answer + 1) * (answer + 1)
    return int(answer)


N = 121

print(solution(N))