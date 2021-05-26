# [Dijkstra] 최소비용 구하기 - 백준 1916

import heapq

N = int(input())
M = int(input())

node = [[] for _ in range(N + 1)]

INF = 10000000000

distance = [INF] * (N+1)
visited = [0] * (N+1)

for i in range(M):
    a,b,d = list(map(int,input().split()))
    node[a].append([b,d])

start, end = list(map(int,input().split()))

def dijkstra(start):
    distance[start] = 0
    hq = []
    visited[start] = 1
    for i in node[start]:
        b = i[0]
        d = i[1]
        if(distance[b] > d):
            distance[b] = d
        heapq.heappush(hq,[d,b])

    while hq:
        d, b = heapq.heappop(hq)
        if(visited[b] == 1):
            continue
        if(distance[b] < d):
            continue
        visited[b] = 1
        for j in node[b]:
            nb, nd = j[0], j[1]
            if(distance[nb] > distance[b] + nd):
                distance[nb] = distance[b] + nd
                heapq.heappush(hq,[distance[nb],nb])


dijkstra(start)

print(distance[end])