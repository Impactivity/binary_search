import sys
read = sys.stdin.readline

n,m = map(int, read().split())
video = list(map(int,read().split()))

start = max(video)
end = sum(video)
res = 10 ** 9

while start <= end:
    #블루레이의 크기를 결정
    mid = (start+end) // 2

    cnt = 1
    tmp = 0
    for i in range(n):
        #블루레이 크기보다 작을 경우 비디오를 계속 넣어줌.
        if tmp + video[i] <= mid:
            tmp += video[i]
        else: #그렇지 않은 경우 블루레이 수를 1 증가하고 초기 tmp 값은 video[i]가 된다.
            cnt += 1
            tmp = video[i]
        if cnt > m:
            break

    # 모든 video체킹했으나 블루레이 cnt가 m 보다 작은경우
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= max(video): #mid 값이 Video의 최대값보다 큰 경우에만
            res = min(res,mid) # 현재 res와 mid를 비교하여 최소값을 찾아낸다.

print(res)
