import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(x,y,col,graph):
    global count
    queue = deque()
    queue.append((x,y))

    while queue :
        a,b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            #graph 범위내에서 현재 위치 값이 인자로 들어온 col와 같다면 방문
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == col:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    count += 1


read = sys.stdin.readline
N = int(input())
graph = [read().strip() for _ in range(N)]


visited = [ [0] * N for _ in range(N) ]
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,graph[i][j],graph)
print(count, end=' ')

# graph의 R을 G로 바꿔주고 bfs를 다시 탐색한다.
visited = [ [0] * N for _ in range(N) ]
count = 0
graph2 = [] * N
for i in range(N):
    graph2.append(graph[i].replace("R","G"))

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,graph2[i][j],graph2)
print(count)