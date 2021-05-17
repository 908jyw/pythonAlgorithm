# [binarysearch] 나무 자르기 - 백준 2805

import sys

N, M = list(map(int,sys.stdin.readline().split()))

tree = list(map(int,sys.stdin.readline().split()))

tree.sort()

# print(tree)



def binarysearch(findNum):

    left = 0
    right = len(tree) - 1

    while(left <= right):
        sum = 0
        mid = (left + right) // 2
        for i in range(mid,right+1):
            sum = sum + tree[i] - tree[mid]
        if(sum > findNum):
            left = mid + 1
            result_index = mid
        elif(sum < findNum):
            right = mid - 1
        else:
            return tree[mid]
    return tree[result_index]


print(binarysearch(M))
