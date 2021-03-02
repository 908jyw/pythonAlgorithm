# [String] 문자열 다루기 기본 - 프로그래머스 1단계
str = 'a234'

def solution(s):
    answer = True

    if(len(s) != 4 and len(s) != 6):
        return False
    for i in s:
        if i.isdigit() == False:
            answer = False
            break

    return answer


solution(str)
