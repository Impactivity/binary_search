import sys
read = sys.stdin.readline

# N 명의 아이, M개의 놀이기구 , 마지막아이가 타는 놀이기구의 번호
N,M= map(int, read().split())
times = list(map(int,read().split()))

if N < len(times):
    print(N)
    exit(0)

# 입력 예시1
# 7 2
# 3 2
#
#    0 1 2 3 4 5 6 7 8 9 10 11 12
# 3  1     4     6
# 2  2   3   5   7

# 입력 예시2
# 22 5
# 1 2 3 4 5
#
#      1 2 3 4  5  6  7  8  9  10  11  12
# 1    1 6 7 9 11 14 16 19 20
# 2    2   8   12    17    21
# 3    3     10      18
# 4    4       13          22
# 5    5          15

l = 1
r = 600000000000
tot_time = 0
while l <= r:
    cnt = M
    mid = (r + l) // 2
    for i in range(len(times)):
        cnt += mid // times[i]
    if cnt >= N:
        r = mid - 1
        tot_time = mid
    else:
        l = mid + 1


cnt = M
# tot_time-1 초에 탑승한 아이 수
for i in range(len(times)):
    cnt += (tot_time-1) // times[i]

# 마지막인 tot_time에 탑승한 아이
for i in range(len(times)):
    if tot_time % times[i] == 0:
        cnt += 1
    if cnt == N:
        print(i+1)
        break


