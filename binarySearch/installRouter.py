# [BinarySerch] 공유기 설치 - 백준 2110

N,C = list(map(int,input().split()))

X = []
for i in range(N):
    X.append(int(input()))

X.sort()

def router_count(num):
    count = 1

    cx = X[0]
    for i in range(1,N):
        if(cx + num <= X[i]):
            count += 1
            if(count > C):
                return count
            cx = X[i]
    return count


def bc():

    result = 0
    left = 1
    right = X[len(X)-1] - X[0]

    while left <= right:

        mid = (left + right) // 2
        compare = router_count(mid)
        if(compare>= C):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

print(bc())