# [BFS,DFS] 벽 부수고 이동하기 - 백준 2206
from collections import deque

N, M = list(map(int,input().split()))

board = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]

result = 10 ** 6
def bfs():
    q = deque()
    y = 0
    x = 0
    w = 0
    d = 1
    q.append([y,x,w,d])

    while q:
        cy,cx,w,d = q.popleft()

        visited[cy][cx][w] = d
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(ny<0 or ny>=N or nx<0 or nx>=M):
                continue

            if(board[ny][nx] == 0 and visited[ny][nx][w] == 0):
                    q.append([ny, nx, w, d + 1])
            if(board[ny][nx] == 1 and visited[ny][nx][w] == 0):
                if(w==0):
                    w = 1
                    q.append([ny, nx, w, d + 1])
                if(w==1):
                    continue



bfs()

if(visited[N-1][M-1][0] == 0 and visited[N-1][M-1][1] != 0):
    print(visited[N-1][M-1][1])
if (visited[N - 1][M - 1][0] != 0 and visited[N - 1][M - 1][1] == 0):
    print(visited[N - 1][M - 1][0])
if(visited[N-1][M-1][0] == 0 and visited[N-1][M-1][1] == 0):
    print(-1)
if(visited[N-1][M-1][0] != 0 and visited[N-1][M-1][1] != 0):
    print(min(visited[N-1][M-1][0],visited[N-1][M-1][1]))
