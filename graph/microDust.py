# [BFS,DFS] 미세먼지 안녕! - 백준 17144 삼성기출

import copy

R, C, T = list(map(int,input().split()))


area = [list(map(int,input().split())) for _ in range(R)]

increase = [[0] * C for _ in range(R)]
decrease = [[0] * C for _ in range(R)]

area_bck = copy.deepcopy(area)

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def spread(y,x):

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0<= ny <R and 0 <= nx < C):
            if(area_bck[ny][nx] >= 0):
                increase[ny][nx] = increase[ny][nx] + (area_bck[y][x] // 5)
                cnt += 1

    decrease[y][x] = area_bck[y][x] // 5 * cnt

def clean():
    global area_bck

    for i in range(1,airClaener[0] - 1):
        if(area_bck[i-1][0] > 0):
            area[i][0] = area_bck[i-1][0]
        else:
            area[i][0] = 0

    for i in range(airClaener[1] + 1 ,R -1):
        if(area_bck[i + 1][0] > 0):
            area[i][0] = area_bck[i+1][0]
        else:
            area[i][0] = 0

    for j in range(0,C-1):
        if(area_bck[0][j+1] > 0):
            area[0][j] = area_bck[0][j+1]
        else:
            area[0][j] = 0

    for j in range(0,C-1):
        if (area_bck[0][j+1] > 0):
            area[R-1][j] = area_bck[R-1][j + 1]
        else:
            area[R-1][j] = 0

    for i in range(airClaener[0] - 1):
        if(area_bck[i + 1][C-1] > 0):
            area[i][C - 1] = area_bck[i + 1][C-1]
        else:
            area[i][C-1] = 0

    for i in range(airClaener[1]+1, R):
        if(area_bck[i-1][C-1] > 0):
            area[i][C - 1] = area_bck[i-1][C-1]
        else:
            area[i][C-1] = 0

    for j in range(1,C):
        if(area_bck[airClaener[0]][j-1] > 0):
            area[airClaener[0]][j] = area_bck[airClaener[0]][j-1]
        else:
            area[airClaener[0]][j] = 0

    for j in range(1, C):
        if (area_bck[airClaener[1]][j - 1] > 0):
            area[airClaener[1]][j] = area_bck[airClaener[1]][j-1]
        else:
            area[airClaener[1]][j] = 0

    area_bck = copy.deepcopy(area)

airClaener = []

for t in range(T):
    for i in range(R):
        for j in range(C):
            if(area_bck[i][j] > 0):
                spread(i,j)
            if(t == 0 and area_bck[i][j] == -1):
                airClaener.append(i)


    for i in range(R):
        for j in range(C):
            area[i][j] = area[i][j] + increase[i][j] - decrease[i][j]

    for i in range(R):
        print(area[i])
    print('----')

    increase = [[0] * C for _ in range(R)]
    decrease = [[0] * C for _ in range(R)]

    area_bck = copy.deepcopy(area)
    clean()

    for i in range(R):
        print(area[i])
    print('----')


result = 0
for i in range(R):
    for j in range(C):
        if (area[i][j] > 0):
            result += area[i][j]

print(result)