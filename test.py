




import itertools

num=[]

num.append(list(map(''.join,itertools.permutations('1234', 4))))

print(num)

zzz = sum(num,[])
print(zzz)
print(zzz[0])

answer = 0