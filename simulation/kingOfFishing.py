# [Simulation] 낚시왕 - 백준 17143
import copy

R, C, M = list(map(int,input().split()))

shark = []
shark.append([0,0,0,0,0])
for i in range(M):
    shark.append(list(map(int,input().split())))

# print("---")
# for i in range(M+1):
#     print(shark[i])
# print("---")
# area = []
# for i in range(R+1):
#     area.append([0,0]*(C+1))
#
area = [[[0,0] for _ in range(C+1)] for _ in range(R+1)]
area_zero = [[[0,0] for _ in range(C+1)] for _ in range(R+1)]

for i in range(M+1):
    r, c, s, d, z = shark[i]
    if(i != 0):
        area[r][c][0] = i
        area[r][c][1] = z



# for i in range(R+1):
#     print(area[i])

# r,c,s,d,z
# r,c 상어의 위치
# s 속력
# d 이동방향 1 위 2 아래 3 오른쪽 4 왼쪽
# z 크기

# 물고기 이동 방향
dx = [0,0,0,1,-1]
dy = [0,-1,1,0,0]

# 총 상어 잡은 크기의 합
result = 0

def moveAndFishing(idx):
    minRow = R
    minRowIdx = M+1
    maxSize = 0
    for i in range(M+1):
        r,c,s,d,z = shark[i]

        if(c>idx):
            continue
        elif(c<idx):
            continue
        elif(c==idx):
            if(r <= minRow):
                minRow = r
                minRowIdx = i


    # print('낚시시작',idx)
    # for i in range(R + 1):
    #     print(area[i])
    # print('낚시끝')

    if(minRowIdx == M+1):
        return 0
    else:
        size = shark[minRowIdx][4]
        # 상어를 잡으면 상어는 사라진다.
        area[minRow][idx][0] = 0
        area[minRow][idx][1] = 0
        shark[minRowIdx] = [0,0,0,0,0]

        return size

def moveShark():
    global area
    area_zero_copy = copy.deepcopy(area_zero)

    for i in range(M+1):
        cr, cc, cs, cd, cz = shark[i]
        nr, nc, nd = cr, cc, cd

        s_copy = cs
        if(cr == 0):
            continue
        while cs > 0:
            ny = nr + dy[nd]
            nx = nc + dx[nd]

            if(ny < 1):
                nd = 2
                continue
            elif(ny >= R+1):
                nd = 1
                continue
            elif(nx < 1):
                nd = 3
                continue
            elif(nx >= C+1):
                nd = 4
                continue
            nr = ny
            nc = nx
            cs = cs - 1
        shark[i] = [nr,nc,s_copy,nd,cz]


        if(area_zero_copy[nr][nc][1] == 0):

            #area_zero_copy[cr][cc][0] = 0
            #area_zero_copy[cr][cc][1] = 0
            area_zero_copy[nr][nc][0] = i
            area_zero_copy[nr][nc][1] = cz
        elif(area_zero_copy[nr][nc][1] != 0):
            if(area_zero_copy[nr][nc][1] > cz):

                shark[i] = [0,0,0,0,0]
                #area_zero_copy[cr][cc][0] = 0
                #area_zero_copy[cr][cc][1] = 0

            elif(area_zero_copy[nr][nc][1] < cz):

                shark[area_zero_copy[nr][nc][0]] = [0,0,0,0,0]
                #area_zero_copy[cr][cc][0] = 0
                #area_zero_copy[cr][cc][1] = 0
                area_zero_copy[nr][nc][0] = i
                area_zero_copy[nr][nc][1] = cz


    area = copy.deepcopy(area_zero_copy)
    # print('먹기시작')
    # for i in range(R + 1):
    #     print(area[i])
    # print('먹기끝')




for i in range(1,C+1):
    if(M == 0):
        break
    sum = moveAndFishing(i)
    result = result + sum
    moveShark()

print(result)