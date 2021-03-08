# [BFS,DFS] 보물섬 - 백준 2589

from collections import deque

N, M = list(map(int,input().split()))

island = []
visited = []
for i in range(N):
    island.append(list(map(str,input())))
    visited.append([0]*M)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

max = -1

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = 1

    global max

    while q:
        cy,cx = q.popleft()
        if(visited[cy][cx] > max):
            max = visited[cy][cx]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(ny < 0 or ny >= N or nx < 0 or nx >= M):
                continue
            if(island[ny][nx] == 'L' and visited[ny][nx] == 0):
                q.append([ny,nx])
                visited[ny][nx] = visited[cy][cx] + 1


for i in range(N):
    for j in range(M):
        if(island[i][j] == 'L' and visited[i][j] == 0):
            bfs(i,j)
            visited = [[0] * M for _ in range(N)]

print(max-1)