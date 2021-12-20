import sys
from collections import deque
read = sys.stdin.readline

N = int(input())
graph = [list(map(int, read().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(num,a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] == 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 :
                continue
            # visited값을 1로 표현 num보다 큰 지역만 탐색
            if graph[nx][ny] >= num and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))


count = 0
_min = 0
_max = 0

_min = min(map(min, graph))
_max = max(map(max, graph))

max_area = _min

#최소부터 최대까지 모두 조사
for k in range(_min, _max+1):
    visited = [[0] * (N) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= k and visited[i][j] == 0:
                bfs(k,i,j)
                count += 1

    if count >= max_area:
        max_area = count

print(max_area)



