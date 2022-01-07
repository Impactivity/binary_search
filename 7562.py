import sys
from collections import deque

read = sys.stdin.readline

#나이트가 이동할 수 있는 경우의 수
dx = [1, 2, -1, -2, -1, -2, 1, 2]
dy = [2, 1, 2 , 1, -2, -1, -2, -1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        # 현재 위치 x,y와 count
        a,b = queue.popleft()

        # 목적지에 도착하였을 경우 return
        if a == fin_pos[0] and b == fin_pos[1]:
            print(visited[a][b] - 1)
            return
        # 갈 수 있는 방향으로 모두 queue에 적재
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[a][b] + 1
    return


#테스트 케이스 갯수
n = int(read())

for _ in range(n):
    #size
    size = int(read())
    cur_pos = list(map(int, read().split()))
    fin_pos = list(map(int, read().split()))
    visited = [[0] * size for _ in range(size)]
    bfs(cur_pos[0],cur_pos[1])

