import sys

read = sys.stdin.readline

n,h = map(int, read().split())

up_cnt = [0] * (h+1)
down_cnt = [0] * (h+1)

for j in range(0,n):
    if (j+1) % 2 != 0 : #홀수일 때
        down_cnt[int(read())] += 1
    else: # 짝수일 때
        up_cnt[int(read())] += 1

for i in range(h-1,0, -1):
    down_cnt[i] += down_cnt[i+1]
    up_cnt[i] += up_cnt[i+1]

min_cnt = n
range_cnt = 0

for i in range(1, h+1):
    if min_cnt > down_cnt[i] + up_cnt[h-i+1]:
        min_cnt = down_cnt[i] + up_cnt[h-i+1]
        range_cnt = 1
    elif min_cnt == down_cnt[i] + up_cnt[h-i+1]:
        range_cnt+=1

print(min_cnt, range_cnt)
