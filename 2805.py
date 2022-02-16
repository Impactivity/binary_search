import sys
read = sys.stdin.readline

n,m = map(int, read().split())
height = list(map(int, read().split()))

l = 1
r = max(height)
mid = 0
while l <= r:
    mid = (l+r) // 2
    tot = 0
    for tree in height:
        if tree >= mid:
            tot += tree - mid

    # m보다 크거나 같은 절단기 높이의 최대 값
    if tot < m:
        r = mid - 1
    else: #tot가 m 보다 작을때까지 l값을 증가시킴
        l = mid + 1

print(r)
