




import itertools

num=[]

num.append(list(map(''.join,itertools.permutations('1234', 4))))

c = list(map(''.join,itertools.permutations('1234', 4)))

print('c', c)


print(num)

zzz = sum(num,[])

print(zzz)

a=[[1,2,3]]

b = sum(a,[])
print(b)


answer = 0


c = list(map(''.join,itertools.permutations('abcd', 4)))

print('c', c)


