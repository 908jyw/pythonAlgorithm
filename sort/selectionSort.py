# [정렬] 선택정렬 - 이것이 코딩테스트다
# 가장 작은 데이터를 찾아서 앞으로 보내는 과정을 N-1번 반복하는 정렬
# O(N*N)

array = [7,5,9,0,3,1,6,2,4,8]

def selectionSort(arr):

    # for i in range(len(arr)):
    #     min_index = i
    #     for j in range(i+1,len(arr)):
    #         if(arr[j] < arr[min_index]):
    #             min_index = j
    #     temp = arr[min_index]
    #     arr[min_index] = arr[i]
    #     arr[i] = temp
    #
    # print(arr)

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    print(arr)

selectionSort(array)
