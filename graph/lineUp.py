# [TopologySort] 줄 세우기 - 백준 2252

import sys
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))

nodeLine = [0] * (N+1)
node = [[] for _ in range(N+1)]

for i in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    node[a].append(b)
    nodeLine[b] += 1



def topologySort(node,nodeLine):

    q = deque()
    result = []

    for i in range(1,N+1):
        if(nodeLine[i] == 0):
            result.append(i)
            q.append(i)

    for i in range(1,N+1):
        x = q.popleft()
        #print('node = ', len(node[x]))
        if(len(node[x]) > 0):
            for j in node[x]:
                nodeLine[j] -= 1
                if(nodeLine[j] == 0):
                    result.append(j)
                    q.append(j)

    return result

result = topologySort(node,nodeLine)

for i in result:
    print(i,end=' ')