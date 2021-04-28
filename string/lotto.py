# [String] 로또의 최고 순위와 최저 순위 - 프로그래머스 1단계

def solution(lottos, win_nums):
    answer = []

    cnt = 0
    for i in win_nums:
        if(i in lottos):
            cnt += 1

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
