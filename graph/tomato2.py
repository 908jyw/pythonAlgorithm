# [BFS,DFS] 토마토 - 백준 7569
from collections import deque
import copy


M, N, H = list(map(int,input().split()))

dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,1,-1]
dz = [-1,1,0,0,0,0]


board = []

for k in range(H):
    a = []
    for i in range(N):
        a.append(list(map(int,input().split())))
    board.append(a)

visited = copy.deepcopy(board)

max_num = 1

def bfs(q):
    global max_num

    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if(nz<0 or nz>=H or ny<0 or ny>=N or nx<0 or nx>=M):
                continue
            if(visited[nz][ny][nx] == 0 and board[nz][ny][nx] == 0):
                q.append([nz,ny,nx])
                visited[nz][ny][nx] = visited[z][y][x] + 1
                if(max_num<visited[nz][ny][nx]):
                    max_num = visited[nz][ny][nx]
        # print('---')
        # for i in range(H):
        #     print('i = ' , i)
        #     for j in range(N):
        #         print(visited[i][j])


q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if(board[k][i][j] == 1):
                q.append([k,i,j])


bfs(q)
chk = False

for k in visited:
    if (chk == True):
        break
    for i in k:
        if(0 in i):
            print(-1)
            chk = True
            break

if(chk == False):
    print(max_num - 1)