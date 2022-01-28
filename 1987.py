import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    global answer
    q = set([(x,y,graph[x][y])])

    while q:
        x,y,ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > R-1 or ny < 0 or ny > C-1:
                continue

            if graph[nx][ny] not in ans:
                q.add((nx,ny,ans + graph[nx][ny] ))
                answer = max(answer, len(ans) + 1 )
    return

read = sys.stdin.readline

R,C = map(int, read().split())
graph = [list(read().strip()) for _ in range(R)]

answer = 1
bfs(0,0)
print(answer)