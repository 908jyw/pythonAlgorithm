# [COMBINATIONS] 소수 만들기 - 프로그래머스


import itertools

a = ['1','2','3','4']
# arr = itertools.combinations(a,3)
arr = list(map(''.join, itertools.combinations(a,3)))

print(arr)

print(arr[0])