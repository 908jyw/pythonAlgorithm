from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(y1,x1,y2,x2):
    q = deque()
    q.append([y1,x1])
    visited[y1][x1] = 1

    while q:
        y, x = q.popleft()

        if (y == y2 and x == x2):
            print(visited[y2][x2] - 1)
            return

        for i in range(8):

            ny = y + dy[i]
            nx = x + dx[i]

            if(0 <= ny < L and 0 <= nx < L):
                if(visited[ny][nx] == 0):
                    q.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1



K = int(input())

for k in range(K):

    L =  int(input())

    visited = []
    for i in range(L):
        visited.append([0] * L)


    x1, y1 = map(int,input().split())
    x2, y2 = map(int, input().split())

    bfs(y1,x1,y2,x2)
