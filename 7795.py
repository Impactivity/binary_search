import sys

read = sys.stdin.readline

T = int(read())

def binary_search(num, arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l+r) // 2

        if arr[mid] < num:
            l = mid + 1
        else:
            r = mid

    return

A=[]
B=[]
for i in range(T):
    A.append(sorted(list(map(int , read().split()))))
    B.append(sorted(list(map(int , read().split()))))

print(A,B)