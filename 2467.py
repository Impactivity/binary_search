import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

l = 0
r = n-1
answer = [ abs(arr[l] + arr[r]) , [arr[l], arr[r]] ]

# 투포인터 알고리즘을 이용하여 두 수의 합이 양수이면 r = r-1
# 두 수의 합이 음수이면 l = l + 1 을 해주어 0에 가까운 값을 찾는다.
while l < r:
    mix = arr[l] + arr[r]
    if abs(mix) < answer[0]:
        answer[0] = abs(mix)
        answer[1] = [arr[l],arr[r]]

    if mix < 0 :
        l = l + 1
    elif mix > 0:
        r = r - 1
    else:
        break

print(answer[1][0], answer[1][1] )

