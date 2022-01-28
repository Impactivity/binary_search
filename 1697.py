from sys import stdin
from collections import deque

read = stdin.readline()

N,K = map(int, read.split())

_pos = deque()
_pos.append(N)


MAX = 100000
dist = [0]*(MAX+1)

while _pos:
    x = _pos.popleft()
    if x == K :
        print(dist[x])
        break

    for i in ( x - 1, x + 1, x * 2):
        if 0 <= i <= MAX and not dist[i]:
            dist[i] = dist[x] + 1
            _pos.append(i)
