# [BFS,DFS] 청소년 상어 - 백준 19236 삼성기출

import copy

result = 0

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

def dfs(water, fish, sy, sx, sum):
    cwater = copy.deepcopy(water)
    cfish = copy.deepcopy(fish)

    # 먹음
    target_fish = cwater[sy][sx]
    sd = cfish[target_fish][1][2]

    # 물고기 정보 없애줌
    cfish[target_fish][1][0] = -1
    cfish[target_fish][1][1] = -1
    cfish[target_fish][1][2] = -1
    cwater[sy][sx] = -1

    sum += (target_fish)
    global result
    if(result < sum):
        result = sum

    # 물고기 이동
    for i in range(1,17):
        if(cfish[i][1][0] < 0):
            continue

        cy = cfish[i][1][0]
        cx = cfish[i][1][1]
        cd = cfish[i][1][2]

        ny = cy + dy[cd]
        nx = cx + dx[cd]
        nd = cd

        while (ny < 0 or ny >=4 or nx < 0 or nx >= 4 or (ny==sy and nx==sx)):
            nd = (nd + 1) % 8
            ny = cy + dy[nd]
            nx = cx + dx[nd]

        if(cwater[ny][nx] != -1):
            size = cwater[ny][nx]

            cfish[size][1][0] = cy
            cfish[size][1][1] = cx

            cfish[i][1][0] = ny
            cfish[i][1][1] = nx
            cfish[i][1][2] = nd

            cwater[ny][nx] = i
            cwater[cy][cx] = size

        else:
            cfish[i][1][0] = ny
            cfish[i][1][1] = nx
            cfish[i][1][2] = nd

            cwater[ny][nx] = i
            cwater[cy][cx] = -1

    # 상어 이동
    for i in range(1,4):
        ny = sy + dy[sd] * i
        nx = sx + dx[sd] * i


        # if(0<=ny<4 and 0<=nx<4 and cwater[ny][nx] != -1):
        #     dfs(cwater,cfish,ny,nx,sum)
        # else:
        #     break
        # 위 아래 다른 점 찾기

        if(ny < 0 or ny >= 4 or nx < 0 or nx >= 4):
            break
        if(cwater[ny][nx] != -1):
            dfs(cwater, cfish, ny, nx, sum)


# board 테이블, fish 정보 테이블 필요
inpu = []
for i in range(4):
    inpu.append(list(map(int,input().split())))

water = [[0] * 4 for _ in range(4)]
fish = [[[0],[-1,0,0]] for _ in range(17)]

# 초기 입력값 세팅
for i in range(4):
    for j in range(8):
        if(j % 2 == 0):
            water[i][j // 2] = inpu[i][j]
            fish[inpu[i][j]][0] = inpu[i][j]
        else:
            fish[inpu[i][j-1]][1][0] = i
            fish[inpu[i][j-1]][1][1] = j // 2
            fish[inpu[i][j-1]][1][2] = inpu[i][j] - 1

dfs(water, fish, 0, 0, 0)

print(result)