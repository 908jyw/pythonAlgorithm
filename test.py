# 테스트 파이썬 파일

arr = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(10,-1,-1):
    print('i=',i)
    if i == 7:
        del arr[i]
    print(arr[i])


print('--')
#
# for i in range(len(arr)):
#     print('len 초기 = ', len(arr))
#     print('i=',i)
#     print(arr[i])
#     if i == 7:
#         print(arr[i])
#         po = arr.pop(i)
#         print('po = ',po)
#         #del arr[i]
#         print(arr)
#     print(arr[i])