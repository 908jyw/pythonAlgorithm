# [COMBINATIONS] 소수 만들기 - 프로그래머스
#
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항



result = [0] * 3

global_num = []

nums = [1,2,3,4]

prime = [2]

cnt = 0

def isPrime(n):
    if(n == 1):
        return False
    if(n in prime):
        return True
    for i in range(2,n):
        if (n % i == 0):
            return False
    prime.append(n)
    return True

def dfs(index, depth):
    # global global_num

    if(depth < 2):
        result[depth] = global_num[index]
        #print(depth, result[depth])
        for i in range(index,len(global_num)):
            if(i!=index):

                dfs(i,depth+1)
    else:
        result[depth] = global_num[index]
        #print(result)
        global cnt
        if(isPrime(sum(result)) == True):
            cnt += 1


def solution(nums):
    answer = -1
    global global_num

    global_num = nums
    for i in range(len(global_num)):
        dfs(i,0)

    return answer



solution(nums)

print(cnt)



# 다른 사람 풀이 추가
# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer