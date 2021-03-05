# [String] 서울에서 김서방 찾기 - 프로그래머스 1단계


S = ["Jane", "Kim"]

def solution(seoul):
    answer = ''
    answer = "김서방은 " + str(seoul.index("Kim")) + "에 있다"

    return answer


result = solution(S)

print(result)