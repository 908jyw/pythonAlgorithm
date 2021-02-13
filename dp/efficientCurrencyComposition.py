# [DP] 효율적인 화폐 구성 - 이것이 코딩테스트다 P226


N, M = list(map(int,input().split()))

currency = []

result = [-1] * 16

for i in range(N):
    currency.append(int(input()))

currency.sort()


for i in range(N):
    result[currency[i]] = 1

for i in range(M+1):
    for j in range(N):
        if(i not in currency and result[i-currency[j]] != -1):
            if (result[i] != -1):
                result[i] = min(result[i-currency[j]] + 1 , result[i])
            else:
                result[i] = min(result[i-currency[j]] + 1 , 10001)

print(result[M])