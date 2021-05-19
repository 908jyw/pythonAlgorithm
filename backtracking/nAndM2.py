# [Backtracking] N과 M(2) - 백준 15650

# N, M = list(map(int,input().split()))
#
# arr = [0] * (M+1)
#
# def dfs(num,depth):
#     if(depth < M+1):
#         for i in range(1,N+1):
#             if(i > num):
#                 arr[depth] = i
#                 dfs(i,depth+1)
#     else:
#         for i in range(1,M+1):
#             print(arr[i], end=' ')
#         print('')
#
# dfs(0, 1)





import sys
import copy

N,M = list(map(int,sys.stdin.readline().split()))

visited = [0] * (N+1)
result = [0] * (M+1)

def dfs(depth,num,visited):
    visited_copy = copy.deepcopy(visited)
    visited_copy[num] = 1

    if(depth < M):
        result[depth] = num
        for i in range(num+1,N+1):
            if(visited_copy[i] == 0):
                dfs(depth+1,i,visited_copy)
    else:
        result[depth] = num
        for i in range(1,M+1):
            print(result[i],end=' ')
        print()



for i in range(1,N+1):
    dfs(1,i,visited)