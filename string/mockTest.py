# [String] 모의고사 - 프로그래머스 1단계

arr = [1,3,2,4,2]

def solution(answers):
    answer = []

    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]

    result_1 = 0
    result_2 = 0
    result_3 = 0

    for i in range(len(answers)):
        if(answers[i] == student_1[i]%5):
            result_1 += 1
        if(answers[i] == student_2[i]%8):
            result_2 += 1
        if(answers[i] == student_3[i]%10):
            result_3 += 1

    MAX = max(result_1,result_2,result_3)



    return answer

solution(arr)