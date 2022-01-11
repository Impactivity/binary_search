import sys
sys.setrecursionlimit(1000000)

from collections import deque

read = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    queue = deque()
    queue.append([0,0,1])

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while queue:
        x,y,w = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                #현재 graph값이 1이고 벽을 허물 수 있다면 (w==1)
                if graph[nx][ny] == 1 and w == 1 :
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append([nx,ny,0])
                #graph값이 0 이고 방문하지 않은 상태면
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx,ny,w])

    return -1

n,m = map(int, read().split())

graph = [ list(map(int, read().strip())) for _ in range(n) ]

print(bfs())