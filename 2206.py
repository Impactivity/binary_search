import sys
from collections import deque

read = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs():
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx > n-1 or ny < 0 or ny < m-1:
                continue



n,m = map(int, read().split())

visited = [[0]*n for _ in range(m)]

graph = [ list(map(str, read().split())) for _ in range(n)]

print(graph)