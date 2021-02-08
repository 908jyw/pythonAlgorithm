# [BFS,DFS] 아기상어 - 백준 16236 삼성기출

from collections import deque

N = input()

water = []
visited = []

size = 2
size_count = 0

# 방향 설정
dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 초기 입력값 설정
for i in range(N):
    water.append(list(map(int,input().split())))
    visited.append([0]*N)

def bfs(y,x):
    q = deque



for i in range(N):
    for j in range(N):
        if(water[i][j] == 9 and visited[i][j] == 0):
            bfs(i,j)