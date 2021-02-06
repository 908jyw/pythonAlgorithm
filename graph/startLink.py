# 백준 5014 스타트링크


from collections import deque

# 전체F층 목적지G층 지금있는곳S층 U, D
F, S, G, U, D = map(int,input().split())
visited = [0] * (F+1)
visited[0] = 1

dx = [U,-D]

def bfs(f,s,g,u,d,b):
    q = deque()
    q.append(s)
    count = 0
    visited[s] = 1
    while q:
        s = q.popleft()
        if(s == g):
            print(visited[s] - 1)
            b = True
            return b
            break
        for i in range(2):
            ns = s + dx[i]
            if(1 <= ns <= F and visited[ns] == 0):
                visited[ns] = visited[s] + 1
                q.append(ns)
    return False

B = False
B = bfs(F,S,G,U,D,B)
if(B == False):
    print("use the stairs")