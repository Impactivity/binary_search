import sys

read = sys.stdin.readline

n = int(read())
arr = [0] + list(map(int, read().split()))
dp = [0 for _ in range(n+1)]
tmp = [-1000000001]
maxVal = 0
def binary_search(tmp, num):
    start = 0
    end = len(tmp) - 1

    while start < end:
        mid = (start+end) // 2

        if tmp[mid] < num:
            start = mid + 1
        else:
            end = mid

    return end


for i in range(1,n+1):
    if tmp[-1] < arr[i]: #현재 수가 부분수열 마지막 수 보다 크다면
        tmp.append(arr[i]) # 부분수열에 append
        dp[i] = len(tmp) - 1 # 부분수열에 초기값 뺀 나머지 길이를 저장
        maxVal = dp[i] # 부분수열 최대길이를 maxVal에 저장
    else:
        dp[i] = binary_search(tmp,arr[i]) #tmp에서 현재 수 를 찾아
        tmp[dp[i]] = arr[i] #해당 수로 갱신..

print(maxVal)

answer = []
for i in range(n,0,-1):
    if dp[i] == maxVal:
        answer.append(arr[i])
        maxVal -= 1

print(*answer[::-1])