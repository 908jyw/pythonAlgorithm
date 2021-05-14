# [정렬] 삽입정렬 - 이것이 코딩테스트다
# O(N*N)

array = [7,5,9,0,3,1,6,2,4,8]


# 삽입 정렬은 리스트의 두번째 인자부터 시작하여, 비교를 하며 자리를 스위치 하면서 선택된 인자가 삽입될 공간을 찾는다.
# 첫번째 포문에서 비교대상이 될 인자를 선택하고, while 문을 통해 선택된 인자의 값보다 큰값이 있으면, 자리를 바꾸는 식으로 진행한다.
def insertSort(arr):

    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j != 0:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1

    print(arr)

insertSort(array)