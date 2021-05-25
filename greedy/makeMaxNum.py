# [Numeric] 큰 수 만들기 - 프로그래머스

from collections import deque


def solution(number, k):
    answer = ''

    n = len(number)
    leng = n - k
    if (leng < 0):
        return number
    index = 0
    pick = 0
    q = deque()

    # i = 0,1,2,3,4,5,6,7,8
    # 8654 까지 들어갔다가
    # 654 빼고 71234

    compare_num = 0
    for i in range(len(number)):

        if (i <= k):
            if (int(number[i]) > int(compare_num)):
                q.clear()
                q.append(number[i])
                compare_num = number[i]
                continue
            else:
                while True:
                    temp = q.pop()
                    if (int(temp) >= int(number[i])):
                        q.append(temp)
                        q.append(number[i])
                        break
        if (k < i):

            if (len(q) > i - k):
                compare_num = q[i - k]
            else:
                if (n - i <= leng - len(q)):
                    q.append(number[i])
                    continue

            if (int(number[i]) > int(compare_num)):
                while len(q) > i - k:
                    temp = q.pop()
                    if (len(q) == i - k):
                        q.append(number[i])
                        break
            else:
                while True:
                    temp = q.pop()
                    if (int(temp) >= int(number[i])):
                        q.append(temp)
                        q.append(number[i])
                        break

    while q:
        answer += q.popleft()

    if (len(answer) > leng):
        answer = answer[:leng]

    return answer

number = "865471234"
k = 3

solution(number,k)