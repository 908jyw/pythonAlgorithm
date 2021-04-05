# [Simulation] 컨베이어 벨트 위의 로봇 - 백준 20055 삼성기출

N, K = list(map(int,input().split()))

# 내구도
A = list(map(int,input().split()))


# 로봇의 위치
robot = []
print(len(robot))


# 벨트가 회전한다.
def lotation():
    print('lotation',robot)
    for i in range(len(robot)):

        cx = robot[i][0]
        nx = cx + 1


        if(nx >= 2*N):
            nx = 0


        # 다음칸의 내구도가 0이거나, 로봇이 있으면
        if(A[nx] == 0):
            continue
        break_boolean = False
        for j in range(len(robot)):
            pre_robot = robot[i][0]
            if(pre_robot == nx):
                break_boolean = True
                break
        if(break_boolean == True):
            continue

        robot[i][0] = nx
        A[nx] = A[nx]-1


# 올라가는 위치에 로봇이 없으면 로봇을 올린다
def makeRobot():
    print('makeRobot', robot)
    make_boolean = True
    for i in range(len(robot)):
        if(robot[i][0]==0):
            make_boolean = False
            break

    if(make_boolean == True):
        robot.append([0])
    print('makeRobot', robot)

def chkA():
    print('makeRobot A=', A)
    cnt = 0
    global finish_boolean
    finish_boolean = False
    for i in range(len(A)):
        if(A[i] == 0):
            cnt += 1
        if(cnt >= K):
            finish_boolean = True
            break


finish_boolean = False
result = 0

while(finish_boolean == False):
    lotation()
    makeRobot()
    chkA()
    result += 1
#
# lotation()
# makeRobot()
# chkA()
# result += 1
# print(finish_boolean)
#
# lotation()
# makeRobot()
# chkA()
# result += 1
# print(finish_boolean)
#
# lotation()
# makeRobot()
# chkA()
# result += 1
# print(finish_boolean)

print(result - 1)

