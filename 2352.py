import sys
from bisect import bisect_left

read = sys.stdin.readline

n = int(read())
port = list(map(int, read().split()))

lis = [port[0]]

for i in range(1,n):
    if lis[-1] < port[i]:
        lis.append(port[i])
    else:
        lis[bisect_left(lis,port[i])] = port[i]
print(len(lis))

