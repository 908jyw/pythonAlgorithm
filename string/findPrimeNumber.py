# [String] 소수 찾기 - 프로그래머스 1단계

N = 100

def solution(n):
    answer = 0
    primeNum = [2]

    for i in range(3,n+1):
        for j in primeNum:
            if ((i // 2) < j):
                primeNum.append(i)
                break
            if(i % j == 0):
                break
            if(j == primeNum[len(primeNum)-1]):
                print(i)
                primeNum.append(i)

    answer = len(primeNum)
    return answer


result = solution(N)

print(result)