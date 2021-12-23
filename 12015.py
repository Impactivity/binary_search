import sys
read = sys.stdin.readline

N = int(input())
A = list(map(int, read().split()))
stack = [0]


def binary_search(target):
    start = 1
    end = len(stack) - 1
    while start <= end:
        mid = (start + end)//2
        if target < stack[mid] :
            end = mid - 1
        else : #target >= stack[mid]
            start = mid + 1
    return end


for a in A:
    if stack[-1] < a :
        stack.append(a)
    else :
        stack[binary_search(a)] = a

print(len(stack) - 1) #-1 해서 0을 뺴주기



def find(target):
    l, h = 1, len(stack)-1
    while l < h:
        m = (l+h)//2
        if stack[m] < target:
            l = m+1
        elif stack[m] > target:
            h = m
        else:
            l = h = m
    return h

l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]
for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a

print(len(stack)-1)
