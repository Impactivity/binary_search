import sys

read = sys.stdin.readline

x,y,c = map(float, read().split())

#문제에서 삼각비를 이용하여 t1 : c  = t : b  , t2 : c = t : a
# f 함수에서 다음과 같이 도출할 수 있다.

def f(x,y,m):
    a = (x**2 - m**2)**0.5
    b = (y**2 - m**2)**0.5
    c = (a*b) / (a+b)

    return c

l = 0
r = min(x,y)
res = 0
while r-l > 0.000001: #문제에서 수는 소수 여섯째 자리까지 주어짐.

    mid = (l+r) / 2

    if f(x,y,mid) >= c:
        res = mid
        l = mid
    else:
        r = mid

print(res)