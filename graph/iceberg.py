# 백준 2573 빙산


from collections import deque
import copy

N, M = map(int,input().split())

iceBerg = []
visited = []
iceBerg_temp = []

for i in range(N):
    iceBerg.append(list(map(int,input().split())))
    visited.append([0]*M)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        y, x = q.popleft()
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(0<=ny<N and 0<=nx<M):
                if(iceBerg[ny][nx] != 0):
                    if(visited[ny][nx] == 0):

                        q.append([ny,nx])


def makeWater():
    for i in range(N):
        for j in range(M):
            if(iceBerg[i][j] != 0):
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if(0<=ny<N and 0<=nx<M):
                        if(iceBerg_temp[ny][nx] == 0):
                            if(iceBerg[i][j] > 0):
                                iceBerg[i][j] -= 1


result = 0

while True:
    count = 0
    bo = False
    for i in range(N):
        for j in range(M):
            if(iceBerg[i][j] != 0 and visited[i][j] == 0):
                count += 1

                if(count == 2):
                    bo = True
                    break
                bfs(i,j)
        if(bo == True):
            break
    if(bo == True):
        print(result)
        break
    if(count == 0):
        print(0)
        break
    visited = []
    for i in range(N):
        visited.append([0]*M)

    result += 1
    iceBerg_temp = copy.deepcopy(iceBerg)
    makeWater()




