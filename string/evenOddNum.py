# [String] 평균 구하기 - 프로그래머스 1단계

N = 3

def solution(num):
    answer = ''
    if(num % 2 == 0):
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer

result = solution(N)

print(result)