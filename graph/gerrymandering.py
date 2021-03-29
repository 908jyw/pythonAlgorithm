# [BFS,DFS] 게리맨더링 2 - 백준 17779 삼성기출

N = int(input())

area = []
for i in range(N):
    area.append(list(map(int,input().split())))

for i in range(N):
    print(area[i])


# d1, d2 >= 1
# 1 <= x <= x+d1+d2 <= N
# 1 <= y-d1 <= y < y+d2 <= N

# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
#
# 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
