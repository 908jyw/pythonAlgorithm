# [binarysearch] 나무 자르기 - 백준 2805

import sys

N, M = list(map(int,sys.stdin.readline().split()))

tree = list(map(int,sys.stdin.readline().split()))

tree.sort()

def binarysearch(findNum):

    left = 0
    right = tree[len(tree)-1]

    while(left <= right):
        sum = 0
        mid = (left + right) // 2
        for i in range(len(tree)):
            if(tree[i] < mid):
                continue
            sum = sum + tree[i] - mid
            if(sum > findNum):
                result = mid
                break
        if(sum > findNum):
            left = mid + 1
        elif(sum < findNum):
            right = mid - 1
        else:
            return mid
    return result



print(binarysearch(M))
