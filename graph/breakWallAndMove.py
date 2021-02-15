# [BFS,DFS] 벽 부수고 이동하기 - 백준 2206
from collections import deque

N, M = list(map(int,input().split()))

board = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

result = 10 ** 6
def bfs():
    q = deque()
    y = 0
    x = 0
    d = 1
    q.append([y,x,d])

    while q:
        cy,cx,cd = q.popleft()
        visited[cy][cx] = 1
        if(cy == N-1 and cx == M-1):
            global result
            if(cd < result):
                result = cd
            break

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(0<=ny<N and 0<=nx<M and visited[ny][nx] == 0):
                if(board[ny][nx] == 0):
                    q.append([ny,nx,cd+1])

for i in range(N):
    for j in range(M):
        if(board[i][j] == 1):
            board[i][j] = 0
            bfs()
            board[i][j] = 1

bfs()
if (result == 10**6):
    print(-1)
else:
    print(result)



#
# result = 10**6
# def dfs(y,x,breakYN, cnt):
#
#     cy = y
#     cx = x
#     cnt += 1
#
#     visited[cy][cx] = 1
#
#     if(cy == N-1 and cx == M-1):
#         global result
#         if(cnt < result):
#             result = cnt
#
#     for i in range(4):
#         ny = cy + dy[i]
#         nx = cx + dx[i]
#
#         if(0<=ny<N and 0<=nx<M and visited[ny][nx] == 0):
#             if(board[ny][nx] == 0):
#                 dfs(ny,nx,breakYN,cnt)
#             elif(board[ny][nx] == 1 and breakYN == False):
#                 dfs(ny, nx, True, cnt)
#                 visited[ny][nx] = 0
#
# dfs(0,0,False,0)
#
#
# print(result)
