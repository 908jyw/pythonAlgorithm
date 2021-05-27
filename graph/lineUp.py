# [TopologySort] 줄 세우기 - 백준 2252

import sys
from collections import deque

# N,M = list(map(int,sys.stdin.readline().split()))
#
# nodeLine = [0] * (N+1)
# node = [[] for _ in range(N+1)]
#
# for i in range(M):
#     a,b = list(map(int,sys.stdin.readline().split()))
#     node[a].append(b)
#     nodeLine[b] += 1
#
#
#
# def topologySort(node,nodeLine):
#W
#     q = deque()
#     result = []
#
#     # 진입차수가 0인 노드를 큐에 삽입
#     for i in range(1,N+1):
#         if(nodeLine[i] == 0):
#             result.append(i)
#             q.append(i)
#
#     # 위상 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문, 중간에 q가 null 이 되면 싸이클이 존재한는 것이다.
#     for i in range(1,N+1):
#         x = q.popleft()
#         #print('node = ', len(node[x]))
#         if(len(node[x]) > 0):
#             for j in node[x]:
#                 nodeLine[j] -= 1
#                 if(nodeLine[j] == 0):
#                     result.append(j)
#                     q.append(j)
#
#     return result
#
# result = topologySort(node,nodeLine)
#
# for i in result:
#     print(i,end=' ')


# 다시 풀어보기
N, M = list(map(int,sys.stdin.readline().split()))

node = [[] for _ in range(N+1)]
result = []
node_line_num = [0] * (N+1)

for i in range(M):
    a, b = list(map(int,sys.stdin.readline().split()))
    node[a].append(b)
    node_line_num[b] += 1


def toporogySort(node,node_line_num):
    q = deque()
    for i in range(1,len(node_line_num)):
        if(node_line_num[i]==0):
            q.append(i)

    for i in range(1,len(node)):
        n = q.popleft()
        result.append(n)

        if(len(node[n]) == 0):
            continue

        for j in range(len(node[n])):
            node_line_num[node[n][j]] -= 1
            if(node_line_num[node[n][j]] == 0):
                q.append(node[n][j])

    return result

result = toporogySort(node,node_line_num)

for i in result:
    print(i,end=' ')