# [BFS,DFS] 연구소3 - 백준 17142



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