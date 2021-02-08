# [String] 나누어 떨어지는 숫자 배열 - 프로그래머스 1단계

arr = [5, 9, 7, 10]
divisor = 5

def solution(arr, divisor):
    answer = []
    for i in arr:
        if (i % divisor == 0):
            answer.append(i)

    if (len(answer) == 0):
        answer.append(-1)
    else:
        answer.sort()

    return answer

result = solution(arr, divisor)

print(result)