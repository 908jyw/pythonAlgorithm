# [BFS,DFS] 스타트택시 - 백준 19238 삼성기출

import heapq
from collections import deque

N, M, F = list(map(int,input().split()))

area = []
area.append(['x']*(N+1))
for i in range(1,N+1):
    area.append(list(map(int,input().split())))
    area[i].insert(0,'x')


taxi = list(map(int,input().split()))

people = []
for i in range(M):

    cy,cx,ny,nx = list(map(int,input().split()))
    people.append([cy,cx,ny,nx])
    area[cy][cx] = 9


print('공간')
for i in range(N+1):
    print(area[i])
print('공간끝')

print('택시')
print(taxi)
print('택시끝')



dy = [-1,0,0,1]
dx = [0,-1,1,0]

# 사람을 태우고 나서 또 dfs
def dfs_after(y,x,f,fy,fx):
    visited_after = [[0]*(N+1) for _ in range(N+1)]

    q = deque()
    visited_after[y][x] = 1
    q.append([y,x,f])

    while q:
        cy,cx,cf = q.popleft()


        if(cf < 0):
            return [-1,-1,-1]

        # 목적지 도착했으면
        if(cy==fy and cx==fx):
            cf = cf + (visited_after[cy][cx]-1) * 2
            return [cy,cx,cf]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nf = cf - 1

            # 범위 벗어나면 continue
            if (ny < 1 or ny >= N + 1 or nx < 1 or nx >= N + 1):
                continue

            # 내가 방문하지 않았고, 벽이 아니면 q에 담기
            if (visited_after[ny][nx] == 0 and area[ny][nx] != 1 and area[ny][nx] != 'x'):
                visited_after[ny][nx] = visited_after[cy][cx] + 1
                q.append([ny,nx,nf])

        print('목적지로 가는 bfs')
        for j in range(len(visited_after)):
            print(visited_after[j])
        print('목적지로 가는 bfs 끝')




def dfs_before(y,x,f):
    visited_before = [[0]*(N+1) for _ in range(N+1)]

    d = 0
    hq = []
    visited_before[y][x] = 1
    heapq.heappush(hq,[d,y,x,f])
    while hq:
        cd,cy,cx,cf = heapq.heappop(hq)

        nf = cf - 1

        # 사람 태우러 가는 길에 연료 바닥이면 -1리턴
        if(nf == 0):
            return -1

        # 현재 위치에 사람이 있으면 태움
        if(area[cy][cx] == 9):
            for i in range(len(people)):
                people_y,people_x,people_ny,people_nx = people[i]
                if(people_y == cy and people_x == cx):
                    new_y,new_x,result_f = dfs_after(cy,cx,cf,people_ny,people_nx)
                    return [new_y,new_x,result_f]

            break


        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = cd + 1
            # 범위 벗어나면 continue
            if(ny < 1 or ny >= N+1 or nx < 1 or nx >= N+1):
                continue
            # 내가 방문하지 않았고, 벽이 아니면 hq에 담기
            if(visited_before[ny][nx] == 0 and area[ny][nx] != 1 and area[ny][nx] != 'x'):
                visited_before[ny][nx] = visited_before[cy][cx] + 1
                heapq.heappush(hq,[nd,ny,nx,nf])

        print('승객 태우러 가는 bfs')
        for j in range(len(visited_before)):
            print(visited_before[j])
        print('승객 태우러 가는 bfs 끝')

new_y,new_x,result_f = taxi[0],taxi[1],F

while result_f > 0:
    new_y,new_x,result_f = dfs_before(new_y,new_x,result_f)


print(result_f)