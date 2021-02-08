# [BFS,DFS] 아기상어 - 백준 16236 삼성기출

# from collections import deque
import heapq

# 초기 입력값 설정
N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

# 방향 설정
dx = [0,-1,0,1]
dy = [-1,0,1,0]



size = 2
eat_count = 0
time = 0

def bfs(y,x):
    hq = []
    heapq.heappush(hq,(0,y,x))

    global size
    global eat_count
    global time
    global visited

    while hq:
        d,y,x = heapq.heappop(hq)

        if(0<area[y][x]<size):
            eat_count += 1
            time += d
            d = 0
            if(eat_count == size):
                size += 1
                eat_count = 0
            area[y][x] = 0
            hq.clear()
            visited = [[False] * N for _ in range(N)]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(0<=ny<N and 0<=nx<N):
                if(area[ny][nx] > size or visited[ny][nx]):
                    continue
                visited[ny][nx] = True
                heapq.heappush(hq,(d+1,ny,nx))


for i in range(N):
    for j in range(N):
        if(area[i][j] == 9):
            bfs(i,j)

print(time)