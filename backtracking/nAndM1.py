# [Backtracking] N과 M(1) - 백준 15649
import copy
from collections import deque

N, M = list(map(int,input().split()))
visited_origin = [0] * (N+1)


def bt(num, depth, visited):
    q = deque()

    visited_copy = copy.deepcopy(visited)
    visited_copy[num] = 1

    for i in range(1,N+1):
        if(i != num and visited_copy[i] == 0):
            q.append(i)

    while q:
        nnum = q.popleft()
        print(nnum, end=' ')
        if(depth < M+1):
            bt(nnum,depth+1, visited_copy)
        else:
            print("")

bt(1, 1, visited_origin)

