# [String] 이차원 배열과 연산 - 백준 17140

import heapq

r,c,k = list(map(int,input().split()))

r = r-1
c = c-1

arr = []

for i in range(3):
    arr.append(list(map(int,input().split())))

print(arr)

y = (len(arr))
x = (len(arr[0]))
time = 0


def addZero(a):
    max = 0
    for i in range(len(a)):
        if(len(a[i]) > max):
            max = len(a[i])

    for i in range(len(a)):
        while(len(a[i]) < max):
            a[i].append(0)



def R():
    for i in range(len(arr)):
        hq = []
        arr_temp = sorted(arr[i])
        initial = arr_temp[0]
        count = 0
        print('arr_temp = ', arr_temp)
        for j in range(len(arr_temp)):
            if(initial == arr_temp[j] and arr_temp[j] != 0):
                count += 1
            else:
                heapq.heappush(hq,[count,initial])
                initial = arr_temp[j]
                count = 1
            if(j == len(arr_temp)-1):
                heapq.heappush(hq,[count,initial])
        arr[i] = []
        while hq:
            cnt, num = heapq.heappop(hq)
            arr[i].append(num)
            arr[i].append(cnt)
            print(cnt,num)

        print('before add =' , arr)

        addZero(arr)
    return

def changeRC(a):
    arr_temp = []
    for i in range(len(a[0])):
        arr_temp.append([0] * len(a))

    for i in range(len(a)):
        for j in range(len(a[i])):
            arr_temp[j][i] = a[i][j]
    return arr_temp

def C():
    global arr
    arr_temp = []
    for i in range(len(arr[0])):
        arr_temp.append([0] * len(arr))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr_temp[j][i] = arr[i][j]

    for i in range(len(arr_temp)):
        hq = []
        arr_temp_temp = sorted(arr[i])
        initial = arr_temp[0]
        count = 0
        for j in range(len(arr_temp_temp)):

            if (initial == arr_temp_temp[j]):
                count += 1
            else:
                heapq.heappush(hq, [count, initial])
                initial = arr_temp_temp[j]
                count = 1
            if(j == len(arr_temp_temp)-1):
                heapq.heappush(hq,[count,initial])

        arr_temp[i] = []
        while hq:
            cnt, num = heapq.heappop(hq)
            arr_temp[i].append(num)
            arr_temp[i].append(cnt)

        addZero(arr_temp)
        arr = changeRC(arr_temp)

    return


while 1:
    if(arr[r][c] == k):
        break

    y = (len(arr))
    x = (len(arr[0]))

    if(y>=x):
        R()
        time += 1
        print('arr = ' , arr)
    else:
        C()
        time += 1





print('time = ', time)