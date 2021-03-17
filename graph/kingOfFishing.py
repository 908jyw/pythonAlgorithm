# [BFS,DFS] 낚시왕 - 백준 17143

R, C, M = list(map(int,input().split()))

shark = []
for i in range(M):
    shark.append(list(map(int,input().split())))

print(R,C,M)

for i in range(M):
    print(shark[i])