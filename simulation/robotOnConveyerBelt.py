# [Simulation] 컨베이어 벨트 위의 로봇 - 백준 20055 삼성기출
import copy


N, K = list(map(int,input().split()))


# 내구도
A = list(map(int,input().split()))



# 로봇의 위치
robot = []
print(len(robot))


# 벨트가 회전한다.
def lotation():

    temp = copy.deepcopy(A)

    for i in range(len(A)):

        nx = i + 1
        if(nx >= 2*N):
            nx = 0
        A[nx] = temp[i]

    #
    # for i in range(len(robot)):
    #
    #     cx = robot[i][0]
    #     nx = cx + 1
    #
    #     if(cx == 0):
    #         continue
    #     if(nx >= 2*N + 1):
    #         robot[i][0] = 0
    #         continue
    #         #nx = 0
    #
    #
    #     # 다음칸의 내구도가 0이거나, 로봇이 있으면
    #     if(A[nx] == 0):
    #         continue
    #     break_boolean = False
    #     for j in range(len(robot)):
    #         pre_robot = robot[j][0]
    #         if(pre_robot == nx):
    #             break_boolean = True
    #             break
    #     if(break_boolean == True):
    #         continue
    #
    #     robot[i][0] = nx
    #     A[nx] = A[nx]-1
    # print('1 lotation robot =', robot)
    # print('1 lotation A=', A)


# 올라가는 위치에 로봇이 없으면 로봇을 올린다
def makeRobot():
    make_boolean = True
    for i in range(len(robot)):
        if(robot[i][0]==1):
            make_boolean = False
            break

    if(make_boolean == True and A[1] > 0):
        robot.append([1])
        #if(A[1] > 0):
        A[1] = A[1] - 1
    print('2 makeRobot robot =', robot)

def chkA():
    print('3 makeRobot A=', A)
    cnt = 0
    global finish_boolean
    finish_boolean = False
    for i in range(len(A)):
        if(A[i] == 0):
            cnt += 1
            print('cnt=',cnt)
        if(cnt >= K):
            finish_boolean = True
            break


finish_boolean = False
result = 0

while(finish_boolean == False):
    print('result =',result)
    lotation()
    makeRobot()
    chkA()
    result += 1
    print('--------')


print(result - 1)

