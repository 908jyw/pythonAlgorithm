# [binarysearch] 수 찾기 - 백준 1920
import sys

N = int(sys.stdin.readline().strip())
N_arr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_arr = list(map(int,sys.stdin.readline().split()))

N_arr.sort()

def binarySearch(n):

    left = 0
    right = len(N_arr) - 1


    while left <= right:
        mid = (left + right) // 2
        if(n > N_arr[mid]):
            left = mid + 1
        elif(n < N_arr[mid]):
            right = mid - 1
        else:
            return 1
    return 0



for i in range(len(M_arr)):
    num = M_arr[i]

    print(binarySearch(num))