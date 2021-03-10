# [BFS,DFS] 연구소2 - 백준 17141

import copy
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = list(map(int,input().split()))

lab = []
visited_dfs = []
visited_bfs = []
MIN = 10**6

chk = False

for i in range(N):
    lab.append(list(map(int,input().split())))
    visited_dfs.append([0]*N)
    visited_bfs.append([-1]*N)

def bfs(lab_bfs,visitied):
    MAX = -1
    q = deque()
    for i in range(N):
        for j in range(N):
            if(lab_bfs[i][j] == 9 and visitied[i][j] < 0):
                visitied[i][j] = 0
                q.append([i,j])

    while q:
        cy,cx = q.popleft()
        if(MAX < visitied[cy][cx]):
            MAX = visitied[cy][cx]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(ny<0 or ny>=N or nx<0 or nx>=N):
                continue
            if((lab_bfs[ny][nx] == 0 or lab_bfs[ny][nx] == 2) and visitied[ny][nx] < 0):
                visitied[ny][nx] = visitied[cy][cx] + 1
                q.append([ny,nx])
    global chk

    for i in range(N):
        for j in range(N):
            if(lab_bfs[i][j] == 0 and visitied[i][j] == -1):
                return -1

    chk = True
    return MAX




def dfs(y,x,depth,visited_origin,lab_origin):
    visited_copy = copy.deepcopy(visited_origin)
    lab_copy = copy.deepcopy(lab_origin)
    visited_copy[y][x] = 1
    if(depth < M-1):
        for i in range(N):
            if (i < y):
                continue
            for j in range(N):
                if(i==y and j<x):
                    continue
                if(lab_copy[i][j] == 2 and visited_copy[i][j] == 0):
                    lab_copy[i][j]=9
                    dfs(i,j,depth+1,visited_copy,lab_copy)
                    lab_copy[i][j] = 2
    else:

        global visited_bfs
        bfs_result = bfs(lab_copy,visited_bfs)
        visited_bfs = [[-1]*N for _ in range(N)]
        global MIN
        if(bfs_result < MIN and bfs_result >=0):
            MIN = bfs_result




for i in range(N):
    for j in range(N):
        if(lab[i][j]==2):
            lab[i][j] = 9
            dfs(i,j,0,visited_dfs,lab)
            lab[i][j] = 2

if(chk == False):
    print(-1)
else:
    print(MIN)