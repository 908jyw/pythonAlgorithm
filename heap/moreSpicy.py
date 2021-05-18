# [heap] 더 맵게 - 프로그래머스

import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for i in scoville:
        heapq.heappush(hq, i)

    while True:
        if (len(hq) == 1):
            a = heapq.heappop(hq)
            if a < K:
                return -1
            else:
                break
        else:
            a = heapq.heappop(hq)
            if (a >= K):
                break
            else:
                b = heapq.heappop(hq)
                x = a + (b * 2)
                heapq.heappush(hq, x)
                answer += 1

    return answer

scoville = [1,3,7,4,2]
K = 7

print(solution(scoville,K))