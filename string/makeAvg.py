# [String] 평균 구하기 - 프로그래머스 1단계

ARR = [1,2,3,4]

def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum = sum + i

    answer = sum / len(arr)

    return answer

result = solution(ARR)

print(result)