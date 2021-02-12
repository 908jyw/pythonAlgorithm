# [DP] 피보나치수열 - 이것이 코딩테스트다 P212

arr = [0] * 100


def dp(x):
    if x == 1: return 1
    if x == 2: return 1

    if(arr[x] > 0):
        return arr[x]

    arr[x] = dp(x-1) + dp(x-2)
    return arr[x]

print(dp(10))