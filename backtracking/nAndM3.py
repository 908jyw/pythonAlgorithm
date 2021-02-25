# [Backtracking] N과 M(3) - 백준 15651

N, M = list(map(int,input().split()))
arr = [0] * (N+1)

def dfs(num,depth):
    if(depth < M+1):
        for i in range(1,N+1):
            arr[depth] = i
            dfs(i,depth+1)
    else:
        for i in range(1,M+1):
            print(arr[i], end=' ')
        print('')

dfs(1,1)