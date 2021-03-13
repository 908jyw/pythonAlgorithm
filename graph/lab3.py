# [BFS,DFS] 연구소3 - 백준 17142



import copy
from collections import deque
from itertools import combinations


dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = list(map(int,input().split()))

lab = []
visited_dfs = []
visited_bfs = []
MIN = 10**6

chk = False

def bfs(visited,graph):
    MAX = -1
    q = deque()

    for i in range(N):
        for j in range(N):
            if(visited[i][j] == 0):
                q.append([i,j])
            if(graph[i][j]==2 and visited[i][j] != '*' and visited[i][j] < 0):
                visited[i][j] = '*'

    while q:
        cy,cx = q.popleft()
        if (MAX < visited[cy][cx] and graph[cy][cx] != 2):
        # if (MAX < visited[cy][cx]):
            MAX = visited[cy][cx]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(ny<0 or ny>=N or nx<0 or nx>=N):
                continue
            # if(graph[cy][cx] == 2 and visited[cy][cx] != 0):
            #     if(visited[cy][cx] + 1 < visited[ny][nx]):
            #         visited[ny][nx] = visited[cy][cx] + 1
            if(graph[ny][nx] == 0 and visited[ny][nx] < 0):
                visited[ny][nx] = visited[cy][cx] + 1
                q.append([ny,nx])
            if(visited[ny][nx] == '*'):
                visited[ny][nx] = visited[cy][cx] + 1
                q.append([ny,nx])


    print('bfs 결과')
    for i in range(N):
        print(visited[i])
    print('bfs 결과 끝')


    global chk

    for i in range(N):
        for j in range(N):
            if(graph[i][j] == 0 and visited[i][j] == -1):
                return -1

    chk = True
    print('MAX=',MAX)
    return MAX


def dfs(y,x,depth,visited,graph,bfsvisited):
    visited_bfs_copy = copy.deepcopy(bfsvisited)
    visited[y][x] = 1

    if depth < M-1:
        for i in range(N):
            if(i<y):
                continue
            for j in range(N):
                if(i==y and j<=x):
                    continue
                if(graph[i][j] == 2 and visited[i][j] == 0):
                    visited_bfs_copy[i][j] = 0
                    dfs(i,j,depth+1,visited,graph,visited_bfs_copy)
                    visited_bfs_copy[i][j] = -1
    else:
        # print('dfs 결과')
        # for i in range(N):
        #     print(visited_bfs_copy[i])
        # print('dfs 결과 끝')

        bfs_result = bfs(visited_bfs_copy,graph)
        # visited_bfs = [[-1] * N for _ in range(N)]

        global MIN
        if(bfs_result < MIN and bfs_result >=0):
            MIN = bfs_result




for i in range(N):
    lab.append(list(map(int,input().split())))
    visited_dfs.append([0]*N)
    visited_bfs.append([-1]*N)

for i in range(N):
    for j in range(N):
        if(lab[i][j]==2):
            visited_bfs[i][j] = 0
            dfs(i,j,0,visited_dfs,lab,visited_bfs)
            visited_dfs = [[0]*N for _ in range(N)]
            visited_bfs = [[-1] * N for _ in range(N)]

if(chk == False):
    print(-1)
else:
    if(MIN == 10**6):
        print(0)
    else:
        print(MIN)