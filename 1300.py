N = int(input())
k = int(input())

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, N+1): #1행부터 n행까지
            cnt += min( mid // i , N)

        if cnt < target:
            start = mid + 1
        else :
            end = mid - 1

    return start

print( binary_search(1,N*N,k))