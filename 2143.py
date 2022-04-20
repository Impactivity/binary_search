import sys, bisect
read = sys.stdin.readline

t = int(read())
n = int(read())
list_a = list(map(int,read().split()))
m = int(read())
list_b = list(map(int,read().split()))

# A의 부분합수열 구하기
A = []
for i in range(n):
    tmp = 0
    for j in range(i,n):
        tmp += list_a[j]
        A.append(tmp)


B = []
for i in range(m):
    tmp = 0
    for j in range(i,m):
        tmp += list_b[j]
        B.append(tmp)

B.sort()

cnt = 0
for i in A:
    diff = t - i
    # diff가 B에서 삽입할 위치 알려줌. diff가 존재할 경우 기존항목의 앞 idx로 리턴
    idx = bisect.bisect_left(B, diff)
    if idx >= len(B):
        continue

    # 조합의 합이 같은 경우가 있을 수 있기 때문에 그 인덱스의 차이를 구해준다.
    idx_right = bisect.bisect_right(B, diff)
    if B[idx] == diff:
        cnt += idx_right - idx
print(cnt)
