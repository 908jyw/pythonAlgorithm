# [Graph] 네트워크 연결 - 백준 1922

import heapq

N = int(input())
M = int(input())

visited = [0] * (N+1)
node = [[] for _ in range(N+1)]


for i in range(M):
    a,b,c = list(map(int,input().split()))
    node[a].append([b,c])
    node[b].append([a,c])

# print(node)


def dijkstra(start):
    min_d = 10 ** 6
    min_index = 0
    hq = []

    for i in range(len(node[start])):
        b, d = node[start][i][0], node[start][i][1]
        heapq.heappush(hq,[d,b])

    visited[start] = 1

    while hq:
        d,b = heapq.heappop(hq)
        if(visited[b] > 0):
            continue
        visited[b] = d

        for i in range(len(node[b])):
            nb, nd = node[b][i][0], node[b][i][1]
            heapq.heappush(hq, [nd, nb])



dijkstra(1)

print(sum(visited)-1)