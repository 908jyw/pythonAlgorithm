# [정렬] 삽입정렬 - 이것이 코딩테스트다
# O(N*N)

array = [7,5,9,0,3,1,6,2,4,8]

def insertSort(arr):

    for i in range(1,len(arr)):
        min_index = i
        for j in range(len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
                break
        temp = arr[min_index]
        arr[i]


insertSort(array)