import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
m = int(read())
find = list(map(int, read().split()))

arr = sorted(arr)

def binary_search(num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if num > arr[mid] :
            start = mid + 1
        elif num < arr[mid] :
            end = mid - 1
        else :
            return 1
    return 0


for n in find:
    print(binary_search(n))