# [graph] 단어 변환 - 프로그래머스

from collections import deque
import copy

min = 1000
visited = []


def compareWord(a, b):
    cnt = 0
    for i in range(len(a)):
        if (a[i] != b[i]):
            cnt += 1
            if (cnt > 1):
                return False
    if (cnt == 1):
        return True
    else:
        return False


def bfs(begin, target, words):
    q = deque()
    global min

    for i in range(len(words)):
        if (visited[i] > 0):
            continue

        if (compareWord(begin, words[i]) == True):
            visited[i] = 1
            q.append([i, visited[i]])

    while q:
        index, visited_size = q.popleft()

        if (words[index] == target):
            if (visited[index] < min):
                min = visited[index]

        for i in range(len(words)):
            if (visited[i] > 0):
                continue

            if (compareWord(words[index], words[i]) == True):
                visited[i] = visited_size + 1
                q.append([i, visited[i]])

    return 0


def solution(begin, target, words):
    global visited
    visited = [0] * len(words)
    bfs(begin, target, words)
    global min
    return min

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))