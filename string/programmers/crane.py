# 프로그래머스 > 코딩테스트연슨 > level1 > 크레인 인형뽑기 게임
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    N = len(board)
    baguni = [-1]


    for k in range(len(moves)):
        j = moves[k]
        for i in range(N):
            if(board[i][j-1] > 0):
                if(board[i][j-1] == baguni[len(baguni)-1]):
                    board[i][j-1] = 0
                    answer += 2
                    baguni.pop()
                    break
                baguni.append(board[i][j-1])
                board[i][j-1] = 0
                break

    return answer

result = solution(board, moves)

print(result)