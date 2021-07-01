# [NUMERIC] 진법 정리

# n진수 -> 10진수
print('n진수 -> 10진수')
print(int('111',2))
print(int('222',3))
print(int('333',4))
print(int('444',5))
print(int('555',6))
print(int('FFF',16))
print()


# 10진수 -> 2,8,16 진수
print("10진수 -> 2,8,16 진수")
print(bin(10))
print(oct(10))
print(hex(10))
print()


# 10진수 -> 2,8,16 진수 (진법 표시 지우기)
print("10진수 -> 2,8,16 진수 (진법 표시 지우기)")
print(bin(10)[2:])
print(oct(10)[2:])
print(hex(10)[2:])
print()



# 10진수 -> n진수
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

print('10진수 -> n진수')
print(convert(10,2))
print(convert(10,3))
print(convert(10,4))
print(convert(10,5))
print()

# n진수 -> n 진수
tmp = string.digits+string.ascii_lowercase
def convertN(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convertN(q, base) + tmp[r]

print('n진수 -> n진수')
print(convert(int('a',16),2))
print(convert(int('4',5),3))
print(convert(int('2',3),4))
print(convert(int('11',2),5))