import sys
from collections import deque

read = sys.stdin.readline

k = int(read())


# visited 배열에 1, -1 로해서 저장하면
# 연속된 수가 같을 경우 no 리턴, 다를 경우 yes리턴
def bfs(start):

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        arr = queue.popleft()

        for i in graph[arr]:
            if visited[i] == 0:
                visited[i] = -visited[arr]
                queue.append(i)
            else:
                if visited[i] == visited[arr]:
                    return False
    return True





for i in range(k):
    v,e = map(int, read().split())
    graph = [ [] for _ in range(v+1)]
    visited = [ 0 for _ in range(v+1)]
    is_true = True
    for j in range(e):
        a,b = map(int,read().split())
        graph[a].append(b)
        graph[b].append(a)

    for k in range(1,v+1):
        if visited[k] == 0:
            if not bfs(k):
                is_true = False
                break
    if is_true == True:
        print("YES")
    else:
        print("NO")

