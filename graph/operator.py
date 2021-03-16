# [BFS,DFS] 연산자 끼워넣기 - 백준 14888

import sys
sys.setrecursionlimit(10**6)

import copy

N = int(input())

num_list = list(map(int,input().split()))

operator_list = list(map(int,input().split()))

MAX = -10**9
MIN = 10**9

def dfs(num,index,operator,result,oper):
    num_copy = copy.deepcopy(num)
    operator_copy = copy.deepcopy(operator)

    global MAX
    global MIN

    if(oper == -1):
        result = num_copy[index]

    # +
    if(oper == 0):
        result = result + num_copy[index]
    # -
    elif(oper == 1):
        result = result - num_copy[index]
    # *
    elif(oper == 2):
        result = result * num_copy[index]
    # /
    elif(oper == 3):
        if(result < 0):
            result = -(-result // num_copy[index])
        else:
            result = result // num_copy[index]

    if(index == len(num_copy) - 1):
        if(result > MAX):
            MAX = result
        if(result < MIN):
            MIN = result

    for i in range(4):
        if(operator_copy[i] > 0):
            operator_copy[i] = operator_copy[i] - 1
            dfs(num_copy,index+1,operator_copy,result,i)
            operator_copy[i] = operator_copy[i] + 1



dfs(num_list,0,operator_list,0,-1)


print(MAX)
print(MIN)