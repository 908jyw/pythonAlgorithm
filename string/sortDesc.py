# [String] 문자열 내림차순으로 배치하기 - 프로그래머스 1단계

s = "Zbcdefg"

def solution(s):
    answer = ''

    answer = ''.join(sorted(s, reverse=True))

    return answer

result = solution(s)

print(result)