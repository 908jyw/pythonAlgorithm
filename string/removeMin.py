# [String] 제일 작은 수 제거하기 - 프로그래머스 1단계

def solution(arr):

    arr.remove(min(arr))
    if(len(arr)==0):
        return [-1]
    else:
        return arr

ARR = [4,3,2,1]

print(solution(ARR))