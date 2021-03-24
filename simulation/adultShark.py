# [Simulation] 어른 상어 - 백준 19237 삼성기출

import copy

# N*N 격자, M마리의 상어, 흔적 크기 k
N, M, K = list(map(int,input().split()))

area = []
for i in range(N):
    area.append(list(map(int,input().split())))


visited = [[[0] * 2 for _ in range(N)] for _ in range(N)]
# visited = [[0,0] * N for _ in range(N)]



# 1 위
# 2 아래
# 3 왼쪽
# 4 오른쪽

# 초기 상어의 방향
init_d = list(map(int,input().split()))

shark = [[0] * 3 for _ in range(len(init_d) +1)]

for i in range(N):
    for j in range(N):
        if(area[i][j] != 0):
            shark[area[i][j]][0] = i
            shark[area[i][j]][1] = j
            shark[area[i][j]][2] = init_d[area[i][j]-1]
            visited[i][j][0] = area[i][j]
            visited[i][j][1] = K




# prior_d = [[[0] * 4 for _ in range(4)] for _ in range(len(init_d) +1)]
# prior_d = [[[0] * 4 for _ in range(4)] for _ in range(len(init_d) +1)]

prior_d = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
for i in range(len(init_d)):
    li = []
    for j in range(4):
        li.append(list(map(int,input().split())))
    prior_d.append(li)

print(shark)

for i in range(M+1):
    print(prior_d[i])

for i in range(len((area))):
    print(area[i])

print('---')

for i in range(N):
    print(visited[i])

print('*****')

dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]

BOOLEAN = True

def eraseSharkSmell():
    global BOOLEAN
    BOOLEAN = False
    for i in range(N):
        for j in range(N):
            # 상어의 크기가 2이상인 상어가 있으면 종료되지 않으므로 boolean 값으로 구분
            if(area[i][j] == 2):
                BOOLEAN = True
            if(visited[i][j][1] == 0):
                continue
            if(visited[i][j][1] > 0 and area[i][j] == 0):
                visited[i][j][1] = visited[i][j][1] - 1
                if(visited[i][j][1] == 0):
                    visited[i][j][0] = 0

    print('---')
    for i in range(N):
        print(visited[i])

def sharkMove():

    visited_copy = copy.deepcopy(visited)

    for i in range(M,0,-1):

        cy, cx, d = shark[i]

        if(d == 0):
            continue

        for j in range(4):
            nd = prior_d[i][d-1][j]

            ny = cy + dy[nd]
            nx = cx + dx[nd]

            if(ny<0 or ny>=N or nx<0 or nx>=N):
                continue


            # 이동을 한곳에 나보다 큰 애가 있으면 그 큰 상어는 먹힌다
            if (area[ny][nx] != 0 and area[ny][nx] > i and visited[ny][nx][1] != 0 and visited_copy[ny][nx][1] == 0):
                shark[area[ny][nx]][0] = 0
                shark[area[ny][nx]][1] = 0
                shark[area[ny][nx]][2] = 0
                visited[ny][nx][0] = 0
                visited[ny][nx][1] = 0

            # for 문을 돌았는데 다음으로 갈 공간이 없으면 내가 남긴 흔적 방향으로 가야됨
            if(j==3 and visited[ny][nx][1] != 0):
                for k in range(4):
                    nd = prior_d[i][d - 1][k]
                    ny = cy + dy[nd]
                    nx = cx + dx[nd]

                    if (ny < 0 or ny >= N or nx < 0 or nx >= N):
                        continue

                    if(visited[ny][nx][0] == i):
                        #shark[area[ny][nx]][0] = 0
                        #shark[area[ny][nx]][1] = 0
                        #shark[area[ny][nx]][2] = 0
                        #visited[ny][nx][0] = i
                        #visited[ny][nx][1] = k
                        break

            if(j != 3 and visited[ny][nx][0] != 0):
                continue

            # 상어 이동 후 공간은 상어가 없음
            area[cy][cx] = 0
            # 상어 이동 후 새로운 공간은 현재 상어가 존재
            area[ny][nx] = i
            # 이동한 칸의 초기 향기는 K
            visited[ny][nx][0] = i
            visited[ny][nx][1] = K
            # 상어 좌표 변경
            shark[i][0] = ny
            shark[i][1] = nx
            shark[i][2] = nd

            break


    print('---')
    for i in range(len((area))):
        print(area[i])
    print('---')
    for i in range(M + 1):
        print(shark[i][2],end=' ')
    eraseSharkSmell()


result = 0
while BOOLEAN == True:
    if(result>1000):
        break
    sharkMove()
    result += 1
    print('result = ',result)

if(result>1000):
    print(-1)
else:
    print(result)
