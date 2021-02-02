# import sys
# sys.setrecursionlimit(10**6)
#
# N = int(input())
#
# rgb = []
# visited = []
# visited_rgb = []
#
# for i in range(N):
#     # rgb 값 입력
#     rgb.append(list(map(str,input())))
#     # 방문 리스트 초기화
#     visited.append([0]*N)
#     visited_rgb.append([0] * N)
#
#
# def dfs(y,x):
#     visited[y][x] = 1
#     if(x+1<N and visited[y][x+1]==0 and rgb[y][x] == rgb[y][x+1]):
#         dfs(y,x+1)
#     if (y + 1 < N and visited[y + 1][x] == 0 and rgb[y][x] == rgb[y + 1][x]):
#         dfs(y+1,x)
#     if (x - 1 >= 0 and visited[y][x - 1] == 0 and rgb[y][x] == rgb[y][x - 1]):
#         dfs(y,x-1)
#     if (y - 1 >= 0 and visited[y - 1][x] == 0 and rgb[y][x] == rgb[y - 1][x]):
#         dfs(y-1,x)
#     return True
#
#
# def dfs_rgb(y,x):
#     visited_rgb[y][x] = 1
#     if(x + 1 < N and visited_rgb[y][x + 1]==0 and ((rgb[y][x] == rgb[y][x+1]) or (rgb[y][x] == 'R' and rgb[y][x+1] == 'G') or (rgb[y][x] == 'G' and rgb[y][x+1] == 'R'))):
#         dfs_rgb(y,x+1)
#     if (y + 1 < N and visited_rgb[y + 1][x] == 0 and ((rgb[y][x] == rgb[y + 1][x]) or (rgb[y][x] == 'R' and rgb[y+1][x] == 'G') or (rgb[y][x] == 'G' and rgb[y+1][x] == 'R'))):
#         dfs_rgb(y+1,x)
#     if (x - 1 >= 0 and visited_rgb[y][x - 1] == 0 and ((rgb[y][x] == rgb[y][x - 1]) or (rgb[y][x] == 'R' and rgb[y][x-1] == 'G') or (rgb[y][x] == 'G' and rgb[y][x-1] == 'R'))):
#         dfs_rgb(y,x-1)
#     if (y - 1 >= 0 and visited_rgb[y - 1][x] == 0 and ((rgb[y][x] == rgb[y - 1][x]) or (rgb[y][x] == 'R' and rgb[y-1][x] == 'G') or (rgb[y][x] == 'G' and rgb[y-1][x] == 'R'))):
#         dfs_rgb(y-1,x)
#     return True
#
# count = 0
# for i in range(N):
#     for j in range(N):
#         if(visited[i][j] == 0):
#             count += 1
#             dfs(i,j)
#
# print(count, end=' ')
#
# count = 0
# for i in range(N):
#     for j in range(N):
#         if(visited_rgb[i][j] == 0):
#             count += 1
#             dfs_rgb(i,j)
#
# print(count)


# import sys
# sys.setrecursionlimit(10**6)
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# count = 0
# count_rgb = 0
#
# N = int(input())
#
# rgb = []
# visited = []
# visited_rgb = []
#
# for i in range(N):
#     rgb.append(list(map(str,input())))
#     visited.append([0] * N)
#     visited_rgb.append([0] * N)
#
#
# def dfs(y,x):
#     visited[y][x] = 1
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0<= nx < N and 0<= ny < N and visited[ny][nx] == 0 and rgb[y][x] == rgb[ny][nx]:
#             dfs(ny,nx)
#
#
#
# def dfs_rgb(y,x):
#     visited_rgb[y][x] = 1
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < N and 0 <= ny < N and visited_rgb[ny][nx] == 0 and ((rgb[y][x] == rgb[ny][nx]) or (rgb[y][x] == 'R' and rgb[ny][nx] == 'G') or (rgb[y][x] == 'G' and rgb[ny][nx] == 'R')):
#             dfs_rgb(ny, nx)
#
# for i in range(N):
#     for j in range(N):
#         if(visited[i][j] == 0):
#             count += 1
#             dfs(i,j)
#
# for i in range(N):
#     for j in range(N):
#         if(visited_rgb[i][j] == 0):
#             count_rgb += 1
#             dfs_rgb(i,j)
#
# print(count, count_rgb)


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