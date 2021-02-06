# 백준 7576 토마토

from collections import deque

M, N = map(int,input().split())



tomato = []
visited = []



for i in range(N):
    tomato.append(list(map(int,input().split())))
    visited.append([0]*M)
#  1 익은 토마토
#  0 익지않은 토마토
#  -1 없는 토마토



q = deque()

def bfs(q):
    maxNum = 1
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0 and visited[ny][nx] == 0):
                q.append([ny,nx])
                tomato[ny][nx] = 1
                visited[ny][nx] = visited[y][x] + 1
                if(visited[ny][nx] > maxNum):
                    maxNum = visited[ny][nx]
    return maxNum

dx = [1,0,-1,0]
dy = [0,1,0,-1]



for i in range(N):
    for j in range(M):
        if(tomato[i][j] == 1 and visited[i][j] == 0):
            visited[i][j] = 1
            q.append([i,j])

maxNum = bfs(q)

chk = False
for i in range(N):
    for j in range(M):
        if(tomato[i][j] == 0):
            chk = True
            break
    if(chk == True):
        print(-1)
        break

if chk == False:
    print(maxNum - 1)




