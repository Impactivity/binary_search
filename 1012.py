#-*- coding: utf-8 -*-

from collections import deque


test_case = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(graph, i, j):
    global dx,dy
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return


for i in range(test_case):
    count = 0
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    for a in range (n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                count += 1
    print(count)
