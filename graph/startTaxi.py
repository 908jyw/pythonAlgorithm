# [BFS,DFS] 스타트택시 - 백준 19238 삼성기출

import heapq

N, M, F = list(map(int,input().split()))

area = []
area.append(['x']*(N+1))
for i in range(1,N+1):
    area.append(list(map(int,input().split())))
    area[i].insert(0,'x')

taxi = []
taxi.append(list(map(int,input().split())))

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



def dfs_before(y,x,f):
    visited_before = [[0]*(N+1) for _ in range(N+1)]

    d = 0
    hq = []
    heapq.heappush(hq,[d,y,x,f])
    while hq:
        cd,cy,cx,cf = heapq.heappop(hq)
        visited_before[cy][cx] = 1
        nf = cf - 1

        # 사람 태우러 가는 길에 연료 바닥이면 -1리턴
        if(cf == 0):
            return -1

        # 현재 위치에 사람이 있으면 태움
        if(area[cy][cd] == 9):
            for i in range(len(people)):
                people_y,people_x,people_ny,people_nx = people[i]
                if(people_y == cy and people_x == cx):
                    dfs_after(cy,cd,cf,people_ny,people_nx)




            break


        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = cd + 1
            # 범위 벗어나면 continue
            if(ny < 1 or ny >= N+1 or nx < 1 or nx >= N+1):
                continue
            # 내가 방문하지 않았고, 벽이 아니면 hq에 담기
            if(visited_before[ny][nx] == 0 and area[ny][nx] != 1):
                heapq.heappush(hq,[nd,ny,nx,nf])




dfs_before(taxi[0],taxi[1],F)