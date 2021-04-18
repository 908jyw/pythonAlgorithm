# [String] 핸드폰 번호 가리기 - 프로그래머스 1단계


def solution(phone_number):
    answer = ''

    for i in range(len(phone_number)):
        if(i < len(phone_number) - 4):
            answer += '*'
        else:
            answer += phone_number[i]


    return answer


phone_number = "01033334444"

print(solution(phone_number))