# [Numeric] 약수의 개수와 덧셈 - 프로그래머스

memo = [0] * 1001

def checkNum(num):
    if (memo[num] != 0):
        return memo[num]

    cnt = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            cnt += 1
    if (cnt % 2 == 0):
        memo[num] = num
    else:
        memo[num] = -num

    return memo[num]


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        answer += checkNum(i)

    return answer

left = 24
right = 27

print(solution(left,right))
