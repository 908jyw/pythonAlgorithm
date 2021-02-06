# 백준 10026 적녹색약

import sys
sys.setrecursionlimit(10**6)
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

count = 0
count_rgb = 0

N = int(input())

rgb = []
visited = []
visited_rgb = []

for i in range(N):
    rgb.append(list(map(str,input())))
    visited.append([0] * N)
    visited_rgb.append([0] * N)


def bfs(y,x):
    q.append([y,x])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(0<= nx < N and 0<= ny < N and visited[ny][nx] == 0 and rgb[y][x] == rgb[ny][nx]):
                bfs(ny,nx)


def bfs_rgb(y, x):
    q.append([y, x])
    visited_rgb[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= nx < N and 0 <= ny < N and visited_rgb[ny][nx] == 0 and ((rgb[y][x] == rgb[ny][nx]) or (rgb[y][x] == 'R' and rgb[ny][nx] == 'G') or (rgb[y][x] == 'G' and rgb[ny][nx] == 'R'))):
                bfs_rgb(ny, nx)

for i in range(N):
    for j in range(N):
        if(visited[i][j] == 0):
            count += 1
            bfs(i,j)

for i in range(N):
    for j in range(N):
        if(visited_rgb[i][j] == 0):
            count_rgb += 1
            bfs_rgb(i,j)

print(count, count_rgb)