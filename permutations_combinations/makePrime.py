# [COMBINATIONS] 소수 만들기 - 프로그래머스

result = [] * 3

def dfs(index,num,depth):

    if(depth < 3):
        for(depth < 3):
            result[depth] = num
        dfs()


def solution(nums):
    answer = -1

    for i in range(nums):
        
        dfs(i,nums[i],0)




    return answer



nums = [1,2,7,6,4]


solution(nums)