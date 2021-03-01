# [DP] 피보나치 수5 - 백준 10870
n = int(input())

arr = [0] * (n+1)

arr[0] = 0


for i in range(1, n+1):
    if(i == 1 or i == 2):
        arr[i] = 1
        continue
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])