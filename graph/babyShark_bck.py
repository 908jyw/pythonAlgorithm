# 백준 16236 아기상어

from collections import deque
import heapq

N = int(input())

area = []
visited = []

for i in range(N):
    area.append(list(map(int,input().split())))
    visited.append([0]*N)


dx = [0,-1,1,0]
dy = [-1,0,0,1]

SIZE = 2

TIME = 0

SIZE_COUNT = 0
#
# global visited



def bfs(y,x):
    q = deque()
    q.append([y,x])

    global SIZE
    global SIZE_COUNT
    global TIME
    global visited

    visited[y][x] = 1

    while q:
        y,x = q.popleft()

        print(y,x)

        print('area')
        for i in range(N):
            print(area[i])

        print('visited')
        for i in range(N):
            print(visited[i])


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(0<=ny<N and 0<=nx<N and visited[ny][nx] == 0):
                print('area[ny][nx] = ' , area[ny][nx] , ' SIZE = ' , SIZE)
                if(area[ny][nx] == 0 or area[ny][nx] == SIZE):
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
                elif(area[ny][nx] > 0 and area[ny][nx] < SIZE):
                    area[ny][nx] = 0
                    TIME = TIME + visited[y][x]
                    print("TIME = " , TIME)
                    SIZE_COUNT += 1
                    if(SIZE_COUNT == SIZE):
                        SIZE += 1
                        SIZE_COUNT = 0
                    visited = []
                    for j in range(N):
                        visited.append([0]*N)
                    q.clear()
                    q.append([ny,nx])
                    visited[ny][nx] = 1
                    break

for i in range(N):
    for j in range(N):
        if(area[i][j] == 9):
            area[i][j] = 0
            bfs(i,j)

print(TIME)

