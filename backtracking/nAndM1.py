# [Backtracking] N과 M(1) - 백준 15649
import copy

N, M = list(map(int,input().split()))
visited_origin = [False] * (N+1)

arr = [0] * (M+1)


def dfs(num, depth, visited):
    visited_copy = copy.deepcopy(visited)
    if(depth!=1):
        visited_copy[num] = True

    if(depth < M+1):
        for i in range(1,N+1):
            if(visited_copy[i] == False): # 위에서 방문하지 않은 경우에는 depth를 늘리고 재귀
                arr[depth] = i
                dfs(i,depth+1,visited_copy)
    else:
        for i in range(1,M+1):
            print(arr[i], end=' ')
        print('')

dfs(1,1,visited_origin)


