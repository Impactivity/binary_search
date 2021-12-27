import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

# binary search를 쓰는 것은 부분수열 리스트 안에서
# 현재 target값이 해당 리스트 오름차순에 맞는
# index를 찾아 값을 바꿔주기 위함이다.

def binary_search(start, end , target):
    if start > end :
        return start

    mid = (start + end) // 2

    if array[mid] < target:
        return binary_search(mid+1 , end , target)
    elif array[mid] == target:
        return mid
    else :
        return binary_search(start, mid-1 , target)

array = []
array.append(A[0])

for i in range(1, N):
    if A[i] > array[-1]:
        array.append(A[i])
    else :
        array[binary_search(0, len(array)-1, A[i])] = A[i]

print(len(array))