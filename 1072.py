# import sys
# read = sys.stdin.readline
#
# x,y = map(int,read().split())
#
# l = 1
# r = 1000000000
#
# z = y * 100 // x
# answer = 0
# while l <= r:
#     mid = (r + l) // 2
#
#     if (y+mid)*100 // (x+mid)  > z:
#         r = mid -1
#         answer = mid
#     else :
#         l = mid + 1
#
# if r == 1000000000:
#     print(-1)
# else:
#     print(answer)


import sys
read = sys.stdin.readline

x,y = map(int,read().split())

l = 1
r = 1000000000

z = y * 100 // x

while l < r:
    mid = (r + l) // 2

    if (y+mid)*100 // (x+mid)  > z:
        r = mid
    else :
        l = mid + 1

if r == 1000000000:
    print(-1)
else:
    print(r)
