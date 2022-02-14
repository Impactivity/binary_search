import sys

read = sys.stdin.readline

x,y,c = map(float, read().split())


def f(x,y,m):
    a = (x**2 - m**2)**0.5
    b = (y**2 - m**2)**0.5
    c = (a*b) / (a+b)

    return c

l = 0
r = min(x,y)
res = 0
while r-l > 0.000001:

    mid = (l+r) / 2

    if f(x,y,mid) >= c:
        res = mid
        l = mid
    else:
        r = mid

print(res)