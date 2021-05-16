# [graph] 연결 요소의 개수 - 백준 11724

import sys
sys.setrecursionlimit(10**6)

N, M = list(map(int,input().split()))

graph = [[] * N for _ in range(N)]
conn = []

# print(graph)

for i in range(0,M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

print(graph)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if(visited[i] == True):
            continue
        else:
            dfs(i)

visited = [False] * (N)
cnt = 0
for i in range(N):
    if(visited[i] == True):
        continue
    else:
        dfs(i)
        cnt += 1
print(cnt)