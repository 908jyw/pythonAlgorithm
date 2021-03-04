# [String] 문자열 내 p와 y의 개수 - 프로그래머스 1단계

S = "pPoooyY"


def solution(s):
    answer = True

    numP = 0
    numY = 0

    for i in s:
        if(i == 'p' or i == 'P'):
            numP += 1
        elif(i == 'y' or i == 'Y'):
            numY += 1

    if(numY != numP):
        answer = False

    return answer

result = solution(S)

print(result)