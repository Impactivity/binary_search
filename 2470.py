import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int,read().split()))

arr.sort()

left = 0
right = n-1
answer = arr[left] + arr[right]
al = left
ar = right

while left < right :
    tmp = arr[left] + arr[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        al = left
        ar = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(arr[al], arr[ar])
