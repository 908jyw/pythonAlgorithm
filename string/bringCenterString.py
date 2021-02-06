# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 제사항
# s는 길이가 1 이상, 100이하인 스트링입니다.


s = 'abcde'

def solution(s):

    answer = ''
    size = int(len(s))
    if(size % 2 == 1):
        answer = s[int(size /2)]
    else:
        answer = s[int(size /2 ) -1] + s[int(size /2)]

    return answer

result = solution(s)

print(result)