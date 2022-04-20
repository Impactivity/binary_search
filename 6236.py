import sys
read = sys.stdin.readline

n,m = map(int,read().split())

arr = [int(read()) for _ in range(n)]

l,r = min(arr), sum(arr)

while l <= r:
    mid = (l+r) // 2
    cnt = 1
    tmp = mid
    # print(f'mid : {mid} , l : {l}, r : {r}')
    for i in range(n):
        if tmp < arr[i] :
            tmp = mid
            cnt += 1
        tmp = tmp - arr[i]
    # print('cnt : ', cnt)
    if cnt > m or mid < max(arr):
        l = mid + 1
    else:
        answer = mid
        r = mid - 1


print(answer)

