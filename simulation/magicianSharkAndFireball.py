# [Simulation] 마법사 상어와 파이어 - 백준 20056 삼성기출
import copy

N, M, K = list(map(int,input().split()))

fireBall = []
fireBall.append([0,0,0,0,0])
# r 행
# c 열
# m 질량
# s 속력
# d 방향

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

for i in range(M):
    fireBall.append(list(map(int,input().split())))

area = [[0]*(N+1) for _ in range(N+1)]

for i in range(M+1):
    print(fireBall[i])

print('---')

for i in range(N+1):
    print(area[i])



def moveFireBall():
    for i in range(M+1):
        if(i==0):
            continue
        r,c,m,s,d = fireBall[i]
        s_origin = s

        if(m==0):
            continue

        while s > 0:
            ny = r + dy[d]
            nx = c + dx[d]

            # 열만 마지막일때
            if(nx>N and 1<=ny<=N):
                nx = 1
            # 행만 마지막일때
            elif(ny>N and 1<=nx<=N):
                ny = 1
            # 열과 행 모두 마지막일때
            elif(nx>N and ny>N):
                nx=1
                ny=1
            # 열만 처음일때
            elif(nx<1 and 1<=ny<=N):
                nx = N
            # 행만 처음일때
            elif(ny<1 and 1<=nx<=N):
                ny = N
            # 열과 행 모두 처음일때
            elif(nx<1 and ny<1):
                nx = N
                ny = N

        fireBall[i] = [ny,nx,m,s_origin,d]



for i in range(K):
    moveFireBall()
