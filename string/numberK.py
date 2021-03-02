# [String] K번째 수 - 프로그래머스 1단계

arr = [1, 5, 2, 6, 3, 7, 4]
comm = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for ar in comm:
        temp = []
        i,j,k = ar[0],ar[1],ar[2]
        for x in range(len(array)):
            if(x>=i-1 and x<=j-1):
                array[x]
                temp.append(array[x])
        temp.sort()
        answer.append(temp[k-1])
    return answer


result = solution(arr,comm)

print(result)