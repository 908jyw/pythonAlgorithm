# [graph] 경로찾기 - 백준 11403
import sys

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

result = [[0] * N for _ in range(N)]

def dfs(n,m):
    visited[m] = True
    for i in range(len(graph[m])):
        if (graph[m][i] == 1 and visited[i] == False):
            result[m][i] = 1
            result[n][i] = 1
            dfs(n,i)

for i in range(N):
    visited = [False] * N
    for j in range(len(graph[i])):
        if(graph[i][j] == 1 and visited[j] == False):
            result[i][j] = 1
            dfs(i,j)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j],end=' ')
    print()

print(result)