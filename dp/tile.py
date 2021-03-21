# [DP] 바닥 공사 - 이것이 코딩테스트다 P223

N = int(input())

arr = [0] * 1001
arr[1] = 1
arr[2] = 3

for i in range(3,N+1):
    arr[i] = arr[i-1] + 2 * arr[i-2]


print(arr[N] % 796796)