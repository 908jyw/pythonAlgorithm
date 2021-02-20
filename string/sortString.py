# [String] 문자열 내 마음대로 정렬하기 - 프로그래머스 1단계

def solution(strings, n):
    answer = []
    print(strings)

    a = []
    for i in range(len(strings)):
        a.append([strings[i][n],strings[i]])
    a.sort()
    for i in range(len(a)):
        answer.append(a[i][1])
    return answer


strings = ["sun", "bed", "car"]
n = 1

solution(strings,n)