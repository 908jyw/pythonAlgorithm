# [Graph] 탈출 - 백준 3055
from collections import deque
import copy

R, C = list(map(int,input().split()))

graph = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

q = deque()
si = 0
sj = 0

for i in range(R):
    s = input()
    for j in range(len(s)):
        graph[i][j] = s[j]
        if(s[j]=='*'):
            visited[i][j] = 1
            q.append([i,j])
        if(s[j]=='S'):
            si = i
            sj = j
visited[si][sj] = 1
q.append([si,sj])

dx = [1,0,-1,0]
dy= [0,1,0,-1]

graph_copy = copy.deepcopy(graph)

result = 'KAKTUS'
while q:
    # print('graph')
    # for i in range(len(graph)):
    #     print(graph[i])
    # print('graph_copy')
    # for i in range(len(graph_copy)):
    #     print(graph_copy[i])
    # for i in range(len(visited)):
    #     print(visited[i])


    cy, cx = q.popleft()
    if(result != 'KAKTUS'):
        break
    # print(cy,cx)

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if(ny<0 or ny >= R or nx < 0 or nx >= C):
            continue
        if(graph_copy[ny][nx] == '*'):
            continue
        if(graph[ny][nx] == 'X'):
            continue
        if(graph[cy][cx] == 'S' and visited[ny][nx] == 0):
            if(graph[ny][nx] == 'D'):
                result = visited[cy][cx] + 1
                break
            graph[ny][nx] = 'S'
            visited[ny][nx] = visited[cy][cx] + 1
            q.append([ny, nx])
        if(graph_copy[cy][cx] == '*' and graph[ny][nx] != 'D'):
            graph_copy[ny][nx] = '*'
            q.append([ny,nx])
            continue




if(result != 'KAKTUS'):
    print(result - 1)
else:
    print(result)


