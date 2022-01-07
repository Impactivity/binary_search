import sys
from collections import deque

read = sys.stdin.readline

m,n,h = map(int, read().split())

graph = []

for _ in range(h):
    graph.append([ list(map(int,read().split())) for _ in range(n) ])

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()

result = -1

def bfs():
    global result

    while queue:
        x,y,z = queue.popleft()
        #2차원 상,하,왼쪽,오른쪽,3차원 위,아래 총 6가지 이동
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
                if graph[nx][ny][nz] == 0 :
                    queue.append((nx,ny,nz))
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    result = max(result, graph[nx][ny][nz])

is_aleady_done = True


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                is_aleady_done = False
            elif graph[i][j][k] == 1:
                queue.append((i,j,k))

# 0값이 존재하지 않을 경우 0출력
if is_aleady_done == True:
    print(0)
    exit(0)

#bfs실행
bfs()

#bfs를 돌았으나 0이 하나라도 있으면 -1출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)

print(result - 1)



# #solution 2 2차원으로 푼 오답코드
# import sys
# from collections import deque
#
# read = sys.stdin.readline
#
# m,n,h = map(int, read().split())
#
# graph = [list(map(int, read().split())) for _ in range(h * n)]
#
#
# dx = [-1, 1, 0, 0, -n , n]
# dy = [0, 0, -1, 1,  0 , 0]
#
# queue = deque()
#
# result = -1
# t = n * h
#
# def bfs():
#     global result
#     while queue:
#
#         a,b = queue.popleft()
#
#         for i in range(6):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if 0 <= nx < n*h  and 0 <= ny < m :
#                 if graph[nx][ny] == 0:
#                     queue.append((nx,ny))
#                     graph[nx][ny] = graph[a][b] + 1
#                     result = max(graph[nx][ny], result)
#
#     return
#
# is_aleady_done = True
#
# for i in range(t):
#     for j in range(m):
#         if graph[i][j] == 0:
#             is_aleady_done = False
#         elif graph[i][j] == 1:
#             queue.append((i,j))
#
# # 0값이 존재하지 않을 경우 0출력
# if is_aleady_done == True:
#     print(0)
#     exit(0)
#
# #bfs실행
# bfs()
#
# #bfs를 돌았으나 0이 하나라도 있으면 -1출력
# for i in range(t):
#     for j in range(m):
#         if graph[i][j] == 0:
#             print(-1)
#             exit(0)
#
# print(result - 1)