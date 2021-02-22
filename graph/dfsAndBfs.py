# [BFS,DFS] DFS와 BFS - 백준 1260
from collections import deque
import sys
sys.setrecursionlimit(10**6)

N,M,V = list(map(int,input().split()))
graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

for i in range(M):
    if (graph[i][0] > graph[i][1]):
        graph[i][0], graph[i][1] = graph[i][1], graph[i][0]

graph.sort()

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in graph:
        if v in i:
            if v == i[0]:
                if(visited_dfs[i[1]] == 0):
                    dfs(i[1])
            else:
                if (visited_dfs[i[0]] == 0):
                    dfs(i[0])

def bfs(v):
    q = deque()
    visited_bfs[v] = 1
    print(v, end=' ')
    for i in graph:
        if v in i:
            if v == i[0]:
                if(visited_bfs[i[1]] == 0):
                    q.append(i[1])
                    visited_bfs[i[1]] = 1
            else:
                if (visited_bfs[i[0]] == 0):
                    q.append(i[0])
                    visited_bfs[i[0]] = 1

    while q:
        vv = q.popleft()
        # if(visited_bfs[vv] == 0):
        print(vv, end=' ')
        visited_bfs[vv] = 1
        for i in graph:
            if vv in i:
                if vv == i[0]:
                    if(visited_bfs[i[1]] == 0):
                        q.append(i[1])
                        visited_bfs[i[1]] = 1
                else:
                    if (visited_bfs[i[0]] == 0):
                        q.append(i[0])
                        visited_bfs[i[0]] = 1

dfs(V)
print('')
bfs(V)