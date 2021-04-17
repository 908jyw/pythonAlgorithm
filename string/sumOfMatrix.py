# [String] 행렬의 덧셈 - 프로그래머스 1단계


def solution(arr1, arr2):
    answer = []

    for i in range(2):
        c = [0] * len(arr1[0])
        a = arr1[i]
        b = arr2[i]

        for j in range(len(a)):
            c[j] = a[j] + b[j]
        answer.append(c)

    return answer

ARR1 = [[1,2],[2,3]]
ARR2 = [[3,4],[5,6]]


print(solution(ARR1,ARR2))