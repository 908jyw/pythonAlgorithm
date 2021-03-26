# [Simulation] 낚시왕 - 백준 17143

R, C, M = list(map(int,input().split()))

shark = []
shark.append([0,0,0,0,0])
for i in range(M):
    shark.append(list(map(int,input().split())))

for i in range(M+1):
    print(shark[i])

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
            break
        elif(c<idx):
            continue
        elif(c==idx):
            if(r <= minRow):
                minRow = r
                if(z > maxSize):
                    if(minRowIdx != M+1):
                        shark[minRowIdx] = [0,0,0,0,0]
                    minRowIdx = i
                    maxSize = z
                elif(z < maxSize):
                    shark[i] = [0,0,0,0,0]
    if(minRowIdx == M+1):
        return 0
    else:
        size = shark[minRowIdx][4]
        # 상어를 잡으면 상어는 사라진다.
        shark[minRowIdx] = [0,0,0,0,0]
        return size

def moveShark():
    for i in range(M+1):
        r, c, s, d, z = shark[i]
        s_copy = s
        if(r == 0):
            continue
        while s > 0:
            ny = r + dy[d]
            nx = c + dy[d]

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

for i in range(1,C+1):
    sum = moveAndFishing(i)
    result = result + sum
    moveShark()