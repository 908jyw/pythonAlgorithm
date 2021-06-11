# [String] 숫자의 합 - 백준 11720

import sys

N = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().strip()))

sum = 0
for i in arr:
    sum += i

print(sum)
