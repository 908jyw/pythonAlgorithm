# [Simulation] 마법사 상어와 파이어 - 백준 20056 삼성기출
import copy

N, M, K = list(map(int,input().split()))

fireBall = []
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



def moveFireBall():
    for i in range(len(fireBall)):
        # if(i==0):
        #     continue
        cr,cc,m,s,d = fireBall[i]
        ny,nx = cr,cc
        s_origin = s

        if(m==0):
            continue

        while s > 0:
            ny = ny + dy[d]
            nx = nx + dx[d]

            # print(i,ny,nx)

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
            # 열은 처음이고, 행은 마지막일때
            elif(nx<1 and ny>N):
                nx = N
                ny = 1
            # 열은 마지막이고, 행은 처음일때
            elif (nx > N and ny < 1):
                nx = 1
                ny = N

            s = s - 1

        fireBall[i] = [ny,nx,m,s_origin,d]

    # print("이동")
    # for i in range(len(fireBall)):
    #     print(fireBall[i])
    # print("이동끝")

odd = [1,3,5,7]
even = [0,2,4,6]

def makeFireBall():
    fireBall_copy = copy.deepcopy(fireBall)

    fireBall_copy.sort()
    fireBall_copy.append([0,0,0,0,0])
    pr, pc, pm, ps, pd = 0,0,0,0,0
    sum_m = 0
    sum_s = 0
    sum_odd = 0
    sum_even = 0
    count = 0

    # print("fireBall_copy")
    # for i in range(len(fireBall_copy)):
    #     print(fireBall_copy[i])
    # print("fireBall_copy 끝")

    for i in range(len(fireBall_copy)):
        r, c, m, s, d = fireBall_copy[i]
        if(m==0 and i != len(fireBall_copy)-1):
            continue
        if(pr!=r or pc!=c):
            if(count>1):
                fireBall.remove([pr, pc, pm, ps, pd])
                nm = sum_m // 5
                ns = sum_s // count
                if(nm > 0):
                    if(sum_odd > 0 and sum_even > 0):
                        fireBall.append([pr, pc, nm, ns, 1])
                        fireBall.append([pr, pc, nm, ns, 3])
                        fireBall.append([pr, pc, nm, ns, 5])
                        fireBall.append([pr, pc, nm, ns, 7])
                    else:
                        fireBall.append([pr, pc, nm, ns, 0])
                        fireBall.append([pr, pc, nm, ns, 2])
                        fireBall.append([pr, pc, nm, ns, 4])
                        fireBall.append([pr, pc, nm, ns, 6])
            pr = r
            pc = c
            pm = m
            ps = s
            pd = d
            sum_s = s
            sum_m = m
            count = 1
            sum_odd = 0
            sum_even = 0
            if(d in odd):
                sum_odd += 1
            elif(d in even):
                sum_even += 1
        elif(pr==r and pc==c):
            fireBall.remove([pr,pc,pm,ps,pd])
            count += 1
            sum_s += s
            sum_m += m
            if (d in odd):
                sum_odd += 1
            elif (d in even):
                sum_even += 1
            pr, pc, pm, ps, pd = r, c, m, s, d

    # print("분리")
    # for i in range(len(fireBall)):
    #     print(fireBall[i])
    # print("분리끝")



for i in range(K):
    # print('',i,'번째')
    moveFireBall()
    makeFireBall()

result = 0
for i in range(len(fireBall)):
    result += fireBall[i][2]


print(result)