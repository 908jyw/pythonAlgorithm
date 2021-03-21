# [DP] 개미 전사 - 이것이 코딩테스트다 P220

# 탑다운 방식
# N = int(input())
#
# food = list(map(int,input().split()))
#
# arr = [0] * (N)
#
# def dp(X):
#     if X == 0:
#         arr[0] = food[0]
#         return arr[0]
#     if X == 1:
#         arr[1] = max(food[0], food[1])
#         return arr[1]
#
#     if arr[X] != 0:
#         return arr[X]
#
#     arr[X] = max(dp(X-1),dp(X-2) + food[X])
#     return arr[X]
#
#
# dp(N-1)
#
# print(arr[N-1])

# 보텀업 방식

N = int(input())
food = list(map(int,input().split()))
arr = [0] * (N)
arr[0] = food[0]
arr[1] = max(food[0],food[1])

for i in range(2,N):
    arr[i] = max(arr[i-1], arr[i-2] + food[i])

print(arr[N-1])