# [Numeric] 8진수 2진수 - 백준 1212

# 8 진수를 입력 받아 2진수로 표현

import sys

num = sys.stdin.readline().strip() # 8진수로된 정수 값을 받아옴
# print(num)
num = '0o' + num # 8진수 표현식으로 변경
# print(num)
num = int(num,8) # 8진수 표현식을 정수로 변경
# print(num)
num = bin(num) # 8진수 정수를 2진수로 변경
# print(num)

for i in range(2,len(num)):
    print(num[i],end='')
