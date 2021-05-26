# [Dijkstra] 최소비용 구하기 - 백준 1916

import heapq

N = int(input())
M = int(input())

node = [[] for _ in range(N + 1)]

INF = 10000000000

# 시작점에서 각 노드까지의 거리를 저장할 변수
distance = [INF] * (N+1)
# 이미 방문한 노드의 연산을 줄이기 위해 생성한 방문 여부 변수
visited = [0] * (N+1)

# 반복문을 통해서 각 노드의 연결된 노드와 거리를 변수에 저장
for i in range(M):
    a,b,d = list(map(int,input().split()))
    node[a].append([b,d])

start, end = list(map(int,input().split()))

# 출발점을 매개변수로 가장 짧은 거리를 구하는 다익스트라 알고리즘 사용
def dijkstra(start):
    distance[start] = 0
    hq = []
    visited[start] = 1

    # 시작 노드와 연결된 노드의 정보를 우선순위 큐에 담는다다
    for i in node[start]:
        b = i[0]
        d = i[1]
        if(distance[b] > d):
            distance[b] = d
        # 가장 짧은 거리부터 반환하기 위해 우선순위 큐 사용
        heapq.heappush(hq,[d,b])

    while hq:
        d, b = heapq.heappop(hq)
        # 이미 방문한 노드면 연산 필요 없음
        if(visited[b] == 1):
            continue
        # 현재 노드를 방문 처리
        visited[b] = 1
        # 현재 노드에서 연결된 노드의 정보를 통해 최소 거리를 갱신하고, 우선순위 큐에 담는
        for j in node[b]:
            nb, nd = j[0], j[1]
            if(distance[nb] > distance[b] + nd):
                distance[nb] = distance[b] + nd
                heapq.heappush(hq,[distance[nb],nb])


dijkstra(start)

print(distance[end])