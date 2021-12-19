import sys

read = sys.stdin.readline

# 3 <= n <= 10000
N = int(input())

# n <= m <= 1,000,000,000
M = list(map(int, read().split()))

#총 금액
tot_amt = int(input())

start = 1
end = max(M)

while start <= end:
    mid = (start + end) // 2
    _sum = 0
    for i in M:
        if i >= mid :
            _sum += mid
        else :
            _sum += i
    #합이 작다는 것은 mid 값을 더 올려도 된다는 뜻.
    if _sum <= tot_amt:
        start = mid + 1
    else :
        end = mid - 1

print(end)

