# [NUMERIC] 비밀지도 - 프로그래머스

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):

        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)

        str = ''
        for j in range(n):
            if (a[j] == '0' and b[j] == '0'):
                str += " "
            else:
                str += "#"
        answer.append(str)

    return answer