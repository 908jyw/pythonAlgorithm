# [binarysearch] 숫자 카드1 - 백준 10815

import sys
import copy

N = int(sys.stdin.readline().strip())
N_arr = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
M_arr = list(map(int,sys.stdin.readline().split()))

N_arr.sort()

def binarysearch(findNum,n_arr):

    arr = copy.deepcopy(n_arr)
    left = 0
    right = len(arr) - 1
    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        if (findNum > arr[mid]):
            left = mid + 1
        elif (findNum < arr[mid]):
            right = mid - 1
        else:
            arr.pop(mid)
            left = 0
            right = len(arr) - 1
            cnt += 1

    return cnt


for i in range(len(M_arr)):
    print(binarysearch(M_arr[i],N_arr),end=' ')