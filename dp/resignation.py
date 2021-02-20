# [DP] 퇴사 - 백준 14501 삼성기출

N = int(input())

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

memo = [0]*(N+1)
if(N-board[0][0] > 0):
    memo[1] = board[0][1]

print(board)
print(memo)
print('--')

