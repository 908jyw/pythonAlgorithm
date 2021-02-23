# [Backtracking] N과 M(1) - 백준 15649

N, M = list(map(int,input().split()))

def bt(node, depth):
    for i in range(node):
        bt()

bt(N, M)