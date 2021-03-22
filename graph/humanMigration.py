# [BFS,DFS] 인구 이동 - 백준 16234 삼성기출

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

BOOLEAN = True
result = 0

def bfs(y,x):

    nationNum = 1
    nationSum = nation[y][x]
    q = deque()
    yxq = deque()
    global BOOLEAN
    visited[y][x] = 1

    q.append([y,x])
    yxq.append([y,x])

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if(ny<0 or ny >= N or nx<0 or nx>=N):
                continue
            if(visited[ny][nx]==0):
                if(L <= abs(nation[cy][cx] - nation[ny][nx]) <=R):
                    BOOLEAN = True
                    nationNum += 1
                    nationSum += nation[ny][nx]
                    visited[ny][nx] = 1
                    yxq.append([ny,nx])
                    q.append([ny,nx])
    while yxq and nationNum != 0:
        cy,cx = yxq.popleft()
        newNationNum = nationSum // nationNum
        nation[cy][cx] = newNationNum
    # print('-결과-')
    # print('nationSum, nationNum = ',nationSum, nationNum)
    # for i in range(N):
    #     print(nation[i])
    # print('-결과끝-')
    # print('-VISITED결과-')
    # for i in range(N):
    #     print(visited[i])
    # print('-VISITED결과끝-')

N,L,R = list(map(int,input().split()))

nation = []
visited = []
for i in range(N):
    nation.append(list(map(int,input().split())))
    visited.append([0] * N)


while BOOLEAN == True:
    BOOLEAN = False
    for i in range(N):
        for j in range(N):
            if(nation[i][j] > 0 and visited[i][j] == 0):
                bfs(i,j)

    if (BOOLEAN == True):
        result += 1
    visited = [[0] * N for _ in range(N)]

print(result)