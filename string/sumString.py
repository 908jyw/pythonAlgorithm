# [String] 자릿수 더하기 - 프로그래머스 1단계

N = 123

def solution(n):
    answer = 0

    while n != 0:
        answer += n % 10
        n = (n - n % 10) // 10


    return answer



result = solution(N)

print(result)
