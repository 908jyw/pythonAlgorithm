# [String] 같은 숫자는 싫어 - 프로그래머스 1단계

arr = [1,1,3,3,0,1,1]
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if (i < len(arr) - 1):
            if (arr[i] != arr[i + 1]):
                answer.append(arr[i])
        else:
            answer.append(arr[i])

    return answer

result = solution(arr)

print(result)