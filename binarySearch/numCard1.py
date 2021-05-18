# [binarysearch] 숫자 카드1 - 백준 10815

import sys

N = int(sys.stdin.readline().strip())
N_arr = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
M_arr = list(map(int,sys.stdin.readline().split()))

N_arr.sort()

def binarysearch(findNum):

    left = 0
    right = len(N_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if (findNum > N_arr[mid]):
            left = mid + 1
        elif (findNum < N_arr[mid]):
            right = mid - 1
        else:
            return 1
    return 0


for i in range(len(M_arr)):
    print(binarysearch(M_arr[i]),end=' ')