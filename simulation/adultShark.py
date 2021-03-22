# [Simulation] 어른 상어 - 백준 19237 삼성기출

N, M, K = list(map(int,input().split()))

area = []
for i in range(N):
    area.append(list(map(int,input().split())))

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




# prior_d = [[[0] * 4 for _ in range(4)] for _ in range(len(init_d) +1)]
# prior_d = [[[0] * 4 for _ in range(4)] for _ in range(len(init_d) +1)]

prior_d = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
for i in range(len(init_d)):
    li = []
    for j in range(4):
        li.append(list(map(int,input().split())))
    prior_d.append(li)

print(shark)

for i in range(len(prior_d)):
    print(prior_d[i])
