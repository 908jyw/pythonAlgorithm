# [Backtracking] N과 M(2) - 백준 15650

N, M = list(map(int,input().split()))

arr = [0] * (M+1)

def dfs(num,depth):
    if(depth < M+1):
        for i in range(1,N+1):
            if(i > num):
                arr[depth] = i
                dfs(i,depth+1)
    else:
        for i in range(1,M+1):
            print(arr[i], end=' ')
        print('')

dfs(0, 1)