# [graph] 다리 만들기- 백준 11724

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]

visited_island = [[0] * N for _ in range(N)]

def divide_island(n,y,x):
    # bfs로 구현
    q = deque()
    visited_island[y][x] = 1
    q.append([n,y,x])

    while q:
        cn, cy, cx = q.popleft()
        graph[cy][cx] = cn

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(ny<0 or ny>=N or nx<0 or nx>=N):
                continue
            if(visited_island[ny][nx] == 1):
                continue
            if(graph[ny][nx] > 0):
                visited_island[ny][nx] = 1
                q.append([cn,ny,nx])


num = 0
for i in range(N):
    for j in range(N):
        if(graph[i][j] > 0 and visited_island[i][j] == 0):
            num += 1
            divide_island(num,i,j)


# for i in range(N):
#     print(graph[i])

min = N * N

def find_island(n,d,y,x):
    q = deque()
    q.append([n,d,y,x])
    visited_water[y][x] = 1
    global min

    while q:
        cn, cd, cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if (ny < 0 or ny >= N or nx < 0 or nx >= N):
                continue
            if (visited_water[ny][nx] == 1):
                continue
            if (graph[ny][nx] != 0 and graph[ny][nx] != cn):
                if(min>cd):
                    min = cd
            if (graph[ny][nx] == 0):
                visited_water[ny][nx] = 1
                q.append([cn,cd+1,ny,nx])



visited_water = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (graph[i][j] > 0 and visited_water[i][j] == 0):
            find_island(graph[i][j],1,i,j)
            visited_water = [[0] * N for _ in range(N)]



print(min-1)