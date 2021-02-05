# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# ord(문자) -> 아스키코드값확인가


# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	"z--"
# 예3	"=.="	"aaa"
# 예4	"123_.def"	"123_.def"
# 예5	"abcdefghijklmn.p"	"abcdefghijklmn"

new_id = "123_.def"

def solution(new_id):
    answer = ''

    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = list(new_id.lower())

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    validation = []

    for i in range(48,58):
        validation.append(i)

    validation.append(45)
    validation.append(46)
    validation.append(95)

    for i in range(97,123):
        validation.append(i)

    i = 0
    while i < len(new_id):
        if(ord(new_id[i]) not in validation):
            del new_id[i]
            if(i != 0):
                i -= 1
            else:
                i = 0
        else:
            i += 1

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    i = 0
    while i < len(new_id):
        if (i < len(new_id) - 1 and new_id[i] == '.' and new_id[i+1] == '.'):
            del new_id[i]
            if (i != 0):
                i -= 1
            else:
                i = 0
        else:
            i += 1

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if(new_id[0] == '.'):
        del new_id[0]
    if(len(new_id) > 0 and new_id[len(new_id) - 1] == '.'):
        del new_id[len(new_id) - 1]

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if(len(new_id) == 0):
        new_id.append('a')

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if (len(new_id) >= 16):
        while len(new_id) > 15:
            new_id.pop()
    if (new_id[len(new_id) - 1] == '.'):
        del new_id[len(new_id) - 1]

    # 6단계 아래와 같이 하는게 더 간결
    # if len(answer) > 15:
    #   answer = answer[:15]
    #   if answer[-1] == '.':
    #       answer = answer[:-1]


    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if(len(new_id) <= 2):
        while len(new_id) < 3:
            new_id.append(new_id[len(new_id)-1])

    answer = "".join(new_id)

    return answer


result = solution(new_id)

print(result)