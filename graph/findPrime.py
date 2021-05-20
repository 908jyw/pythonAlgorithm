import copy

arr = []


def isPrine(num):
    if (num <= 2):
        return False
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True


def make_dfs(depth, leng, numbers):
    #visited = [0] * len(numbers)
    for i in range(len(numbers)):
        global arr
        arr = [0] * leng
        visited = [0] * len(numbers)
        arr[depth] = numbers[i]
        print(arr[depth])
        dfs(depth+1, leng, visited, numbers, i)


def dfs(depth, leng, visited, numbers, index):
    visited_copy = copy.deepcopy(visited)
    visited_copy[index] = 1
    print(depth, leng)
    global arr
    if (depth < leng):
        for i in range(len(numbers)):
            if (visited_copy[i] == 0):
                arr[depth] = numbers[i]
                dfs(depth + 1, leng, visited_copy, numbers, i)

    else:
        #arr[depth] =\
        #arr.append(numbers[index])
        print(arr)


def solution(numbers):
    answer = 0
    for i in range(1, len(numbers)+1):
        make_dfs(0, i, numbers)

    return answer

numbers = "123"
solution(numbers)