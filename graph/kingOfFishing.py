# [BFS,DFS] 낚시왕 - 백준 17143

R, C, M = list(map(int,input().split()))

shark = []
for i in range(M):
    shark.append(list(map(int,input().split())))

shark.sort()

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

# 사람이동하고 물고기 낚시
def moveAndFishing(index):
    for i in range(M):
        r,c,s,d,z = shark[i]
        if(r==0 or c==0):
            continue
        if(c == index):
            shark[i] = [0,0,0,0,0]
            return z
    return 0

# 상어이동
def moveShark():
    for i in range(M):
        r, c, s, d, z = shark[i]
        s_copy = s
        while s > 0:
            ny = dy[d] + r
            nx = dx[d] + c
            if(ny < 1):
                d = 2
                continue
            elif(ny >= R+1):
                d = 1
                continue
            elif(nx < 1):
                d = 3
                continue
            elif(nx >= C+1):
                d = 4
                continue
            r = ny
            c = nx
            s = s - 1
        shark[i] = [r,c,s_copy,d,z]

    shark.sort()
    # print('-상어이동-')
    # for i in range(M):
    #     print(shark[i])
    # print('-상어이동끝-')

    pr, pc, ps, pd, pz = shark[0]
    pindex = 0
    for i in range(1,M):
        r, c, s, d, z = shark[i]

        if(pr == 0 or pc == 0):
            continue

        if(pr == r and pc == c):
            if(pz >= z):
                shark[i] = [0,0,0,0,0]
            else:
                shark[pindex] = [0,0,0,0,0]
                pindex = i
        else:
            pindex = i
            pr, pc, ps, pd, pz = r, c, s, d, z


if(M == 0):
    print(0)
else:
    for i in range(1, C+1):
        sum = moveAndFishing(i)
        # print('--낚시 시작')
        # for j in range(M):
        #     print(shark[j])
        # print('-낚시 끝-')
        result = result + sum
        moveShark()
        shark.sort()

    print(result)