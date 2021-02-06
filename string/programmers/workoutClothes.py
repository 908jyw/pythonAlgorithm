n = 5
lost = 	[5,4,2]
reserve = [2,4]

def solution(n, lost, reserve):
    answer = 0

    #reserve.sort()
    #lost.sort()


    nreserve = set(reserve) - set(lost)
    nlost = set(lost) - set(reserve)

    size = len(nreserve)

    # 이 경우에는 set를 list로 바꿔줘야지 가능
    # for i in range(size):
    #     if ((nreserve[i] - 1) in nlost):
    #         nlost.remove(nreserve[i] - 1)
    #         continue
    #     elif((nreserve[i] + 1) in nlost):
    #         nlost.remove(nreserve[i] + 1)
    #         continue

    for i in nreserve:
        if (i- 1 in nlost):
            nlost.remove(i - 1)
        elif(i+ 1 in nlost):
            nlost.remove(i + 1)

    answer = n - len(nlost)

    return answer

result = solution(n, lost, reserve)

print(result)