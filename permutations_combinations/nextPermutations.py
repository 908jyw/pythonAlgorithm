# [PERMUTATIONS] 다음 순열 - 백준 10972

# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.
#
# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.
#
# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.
#
# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.
#
# 출력
# 첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

# import itertools
#
# N = int(input())
# compare = list(map(str,input().split()))
#
#
# s = ''
# for i in range(N):
#     s = s + compare[i]
#
# num = ''
# for i in range(1,N+1):
#     num = num + str(i)
#
#
# permutations = list(map(''.join,itertools.permutations(num,N)))
#
# for i in range(len(permutations)):
#     if(permutations[i] == s and i < len(permutations) - 2):
#         for j in permutations[i+1]:
#             print(j,end=' ')
#         break
#     if(i == len(permutations) - 1):
#         print(-1)

import copy

N = int(input())
compare = list(map(int,input().split()))

print(compare)

YN = 'N'

result = [0] * (N)

def dfs(num,depth,visited):
    visited_copy = copy.deepcopy(visited)
    visited_copy[num] = 1
    result[depth] = num
    if(depth < N-1):
        for i in range(1,N+1):
            if(visited_copy[i] > 0):
                continue
            dfs(i,depth+1,visited_copy)
    else:

        result[depth] = num
        global YN
        if (YN == 'Y'):
            print('result = ', result)
            YN = 'N'
        # print('11' , result)
        # print('22',compare)
        if(result == compare):
            YN = 'Y'



visited = [0] * (N+1)

for i in range(1,N+1):
    print(i)
    dfs(i,0,visited)




