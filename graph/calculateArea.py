import sys
sys.setrecursionlimit(10**6)

M, N, K = list(map(int,input().split()))


area = []
visited = []

# 최초 공간 초기화
for i in range(M):
    area.append([0]*N)
    visited.append([0]*N)

xylist = []

# 사각형이 들어갈 좌표 입력받음
for i in range(K):
    xylist.append(list(map(int,input().split())))


# 좌표에 따라서 공간의 값을 1로 변경
for i in range(len(xylist)):
    x1 = xylist[i][0];
    y1 = xylist[i][1];
    x2 = xylist[i][2];
    y2 = xylist[i][3];

    for j in range(len(area)):
        if(j < y2 and j >= y1):
            for k in range(len(area[j])):
                if(k < x2 and k >= x1):
                    area[j][k] = 1

def dfs(y,x,size):
    size += 1
    visited[y][x] = 1
    if(x+1<N and visited[y][x+1] == 0 and area[y][x+1] == 0):
        size = dfs(y,x+1,size)
    if(y+1<M and visited[y+1][x] == 0 and area[y+1][x] == 0):
        size = dfs(y+1,x,size)
    if (x-1 >= 0 and visited[y][x-1] == 0 and area[y][x-1] == 0):
        size = dfs(y, x - 1, size)
    if (y - 1 >= 0 and visited[y - 1][x] == 0 and area[y - 1][x] == 0):
        size = dfs(y - 1, x, size)

    return size


count = 0
result = []

for i in range(len(area)):
    for j in range(len(area[i])):
        if(area[i][j] == 0 and visited[i][j] == 0):
            count += 1
            size = 0

            result.append(dfs(i,j,size))

print(count)
result.sort()
for i in range(len(result)):
    print(result[i], end=' ')
