# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기

numbers = [5,0,2,7]

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        if (i == len(numbers) - 1):
            break
        for j in range(i+1,len(numbers)):
            if(numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

print(solution(numbers))

# 참고할 만한 코
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))