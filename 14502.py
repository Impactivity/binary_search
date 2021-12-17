import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

read = sys.stdin.readline

#세로길이 N , 가로길이 M ( 3 <= N , M <= 8)

N,M = map(int, read().split())
graph = [list ( map(int , read().split())) for _ in range (N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

answer = []


def bfs():
    global MAX
    while queue:
        x,y = queue.popleft()
        #상하좌우 이동하여 바이러스 spread
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if imsi_graph[nx][ny] == 0:
                    imsi_graph[nx][ny] = 2
                    queue.append((nx,ny))


zero_place = deque()
virus = deque()
queue = deque()

#graph에서 바이러스 및 미확진 대상 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_place.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i,j))


combi = list(combinations(zero_place, 3))

for com in combi:
    # 세개 벽 세우기
    imsi_graph = deepcopy(graph)
    queue = deepcopy(virus)
    imsi_graph[com[0][0]][com[0][1]] = 1
    imsi_graph[com[1][0]][com[1][1]] = 1
    imsi_graph[com[2][0]][com[2][1]] = 1

    bfs()

    count = 0
    # 그래프에서 0의 개수 구하기
    for a in range(N):
        for b in range(M):
            if imsi_graph[a][b] == 0:
                count += 1

    answer.append(count)

print(max(answer))
#
# def bfs():
#     global MAX
#     queue = deque()
#     visited = [[0] * M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 2:
#                 queue.append((i,j))
#
#     while queue:
#         a,b = queue.popleft()
#
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#
#             if 0 <= nx < N and 0 <= ny < M:
#                 if graph[nx][ny] == 0 and visited[nx][ny] == 0:
#                     queue.append((nx,ny))
#                     visited[nx][ny] = 1
#
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0 and visited[i][j] == 0:
#                 count += 1
#
#     MAX = max(MAX,count)
#
# def wall(index):
#     if index == 3 :
#         bfs()
#         return
#
#     for x in range(N):
#         for y in range(M):
#             if graph[x][y] == 0 :
#                 graph[x][y] = 1
#                 wall(index+1)
#                 graph[x][y] = 0
#
#
# wall(0)
# print(MAX)