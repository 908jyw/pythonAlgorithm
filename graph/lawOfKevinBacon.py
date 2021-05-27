# [Graph] 케빈 베이컨의 6단계 법칙 - 백준 1389

# 첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다.
# 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다.
# 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다.
# A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
# 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다.
# 또, 모든 사람은 친구 관계로 연결되어져 있다.
# 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

# 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다. 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.

from collections import deque

N, M = list(map(int,input().split()))

friend = [[] for _ in range(N+1)]

# num = [[] for _ in range(N+1)]

for i in range(M):
    a, b = list(map(int,input().split()))
    if(a > N or b > N):
        continue
    friend[a].append(b)
    friend[b].append(a)

# print(friend)


def bfs(n):

    q = deque()
    visited[n][n] = 1
    v = visited[n][n]

    # print('n = ', n)

    for i in friend[n]:
        # print('i = ', i)
        nv = v + 1
        visited[n][i] = nv
        q.append([i,nv])

    while q:
        cn, cv = q.popleft()

        # print('cn,cv',cn,cv)
        for i in friend[cn]:
            if(visited[n][i] > 0):
                continue
            nv = cv + 1
            # print('i,nv',i,nv)
            visited[n][i] = nv

            q.append([i,nv])


visited = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    bfs(i)

min = 10 ** 6
min_index = 0
for i in range(1,N+1):
    # print(visited[i])
    if(min > sum(visited[i])):
        min = sum(visited[i])
        min_index = i

print(min_index)