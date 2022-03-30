import sys
from collections import deque

read = sys.stdin.readline

n,m = map(int,read().split())


graph = [ [] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    a,b,c = map(int,read().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

src, dst = map(int,read().split())

l = 1
r = 1000000000
answer = 0

def bfs(weight):

    queue = deque()
    queue.append([src,0])
    visited = [0] * (n+1)
    visited[src] = 1

    while queue:
        node,cost = queue.popleft()

        if node == dst:
            return True

        for next_node,next_cost in graph[node]:
            # 다음으로 이동할 경로의 무게제한이 weight보다 크다면 통과
            if next_cost >= weight:
                if visited[next_node] == 0:
                    queue.append([next_node, next_cost])
                    visited[next_node] = 1

    return False

# binary search를 이용하여
# 최대 중량을 탐색한다.
# bfs로 해당 중량으로 건너는게 가능한지 판별
while l <= r:

    mid = ( l + r ) //2
    if bfs(mid) == True:
        l = mid + 1
        answer = mid
    else:
        r = mid - 1


print(answer)