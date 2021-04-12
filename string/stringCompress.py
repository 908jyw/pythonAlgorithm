# [String] 2020 KAKAO BLIND RECRUITMENT 문자열 압축 - 프로그래머스



def solution(s):
    answer = 0

    half = len(s)//2

    MIN = 1000

    for i in range(1, half + 1):

        start = 0
        end = 0
        pre_s = s[start:end]
        count = 1
        new_s = ""

        while (True):
        #while (end < len(s) - 1):
            start = end
            end = end + i

            print('end = ', end)

            if(end > len(s)):
                print('count = ',count)
                if(count>1):
                    new_s = new_s + str(count) + pre_s
                    if (len(new_s) < MIN):
                        MIN = len(new_s)
                else:
                    new_s = new_s + pre_s
                print('new_s = ', new_s)
                break


            next_s = s[start:end]

            print('next_s = ', next_s)



            if(pre_s == next_s):
                count = count + 1
                pre_s = next_s
            else:
                if(count > 1):
                    new_s = new_s + str(count) + pre_s
                else:
                    new_s = new_s + pre_s
                count = 1
                pre_s = next_s
            print(new_s)

        if(len(new_s) < MIN):
            MIN = len(new_s)

    answer = MIN

    return answer





s = "aabbaccc"

print('len - 1 =',len(s)-1)

result = solution(s)

print(result)