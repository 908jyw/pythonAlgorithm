# [graph] 트리의 부모 찾기 - 백준 11725
import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = list(map(int,sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)


def dfs(n):
    global visited
    visited[n] = 1

    for i in graph[n]:
        if(visited[i] == 1):
            continue
        else:
            parent[i] = n
            dfs(i)



parent = [0] * (N + 1)
visited = [0] * (N + 1)

for i in range(1,N+1):
    visited[i] = 1
    for j in graph[i]:
        if(visited[j] == 1):
            continue
        else:
            parent[j] = i
            dfs(j)


for i in range(2,len(parent)):
    print(parent[i])
