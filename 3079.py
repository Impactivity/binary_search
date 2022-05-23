import sys
read = sys.stdin.readline
n,m = map(int, read().split())
times = [int(read()) for _ in range(n)]

times.sort()

start = 1
end = m * min(times)
answer = end

while start <= end:
    mid = (start + end) // 2 # 심사에 걸린 시간
    total_people = 0

    for i in range(n):
        total_people += mid // times[i] # mid초 동안 심사한 사람의 수

    if total_people >= m: # 주어진 m명 사람보다 많을 때
        end = mid - 1
        answer = min(answer,mid)
    else:
        start = mid + 1

print(answer)