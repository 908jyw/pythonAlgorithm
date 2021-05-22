# [BFS,DFS] 가장 먼 노드 - 프로그래머스

from collections import deque

graph = []
visited = []


def bfs(n):
    global visited
    global graph

    visited[n] = 1
    q = deque()
    q.append(n)

    while q:
        node = q.popleft()

        for i in graph[node]:
            if (visited[i] > 0):
                continue
            visited[i] = visited[node] + 1
            q.append(i)


def solution(n, vertex):
    answer = 0

    global visited
    visited = [0] * (n + 1)

    global graph
    graph = [[] * 1 for _ in range(n + 1)]

    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    bfs(1)

    answer = visited.count(max(visited))

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,vertex))