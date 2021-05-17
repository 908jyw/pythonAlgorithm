# [graph] 알파벳 - 백준 1987
import sys

R, C = list(map(int,sys.stdin.readline().split()))

graph = []
graph=[list(map(lambda x: ord(x)-65,sys.stdin.readline().strip())) for i in range(R)]

# for i in range(R):
#     graph.append(list(map(str,sys.stdin.readline().strip())))
#
# for i in range(R):
#     for j in range(C):
#         graph[i][j] = ord(graph[i][j]) - 65

visited = [[0] * C for _ in range(R)]
alphabet = [0] * 26

dy = [0,1,0,-1]
dx = [1,0,-1,0]

max = 0

def dfs(y,x,m):

    # alphabet_copy = copy.deepcopy(alphabet_dfs)
    # alphabet_copy[ord(graph[y][x]) - 65] = 1

    # visited_copy = copy.deepcopy(visited_dfs)
    # visited_copy[y][x] = 1
    global visited
    global alphabet

    global max
    if(m > max):
        max = m

    cy = y
    cx = x
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if(ny < 0 or ny >= R or nx < 0 or nx >= C):
            continue
        if(alphabet[graph[ny][nx]] == 1):
            continue
        if(visited[ny][nx] == 1):
            continue
        temp = graph[ny][nx]
        visited[ny][nx] = 1
        alphabet[temp] = 1
        dfs(ny,nx,m+1)
        visited[ny][nx] = 0
        alphabet[temp] = 0


alphabet[graph[0][0]] = 1
visited[0][0] = 1
dfs(0,0,1)

print(max)
