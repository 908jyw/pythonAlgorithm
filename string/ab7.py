# [String] A+B - 7 - 백준 11021


import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    a, b = list(map(int,sys.stdin.readline().split()))
    rewult = a + b
    print("Case #",i+1,sep='',end='')
    print(":", rewult)

