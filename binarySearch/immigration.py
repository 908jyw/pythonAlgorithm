# [binarysearch] 입국심사 - 프로그래머스

def soltion(n,times):
    answer = 0
    times.sort()

    left = 1
    right = n * times[len(times)-1]

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid//time

            if(count >= n):
                break

        if count >= n:
            answer = mid
            right = mid - 1

        elif count < n:
            left = mid + 1

    return answer

n = 6
times = [7,10]

print(soltion(n, times))