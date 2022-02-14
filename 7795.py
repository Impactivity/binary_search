import sys

read = sys.stdin.readline

def binary_search(num, k):
    l = 0
    r = k - 1
    res = -1
    while l <= r: #l,r이 같을 때 까지 돌기 때문에 l,r을 각각 mid 값을 기준으로 증감 해줘야 while이 종료됨.
        # 주어진 target값이 arr에서 위치 최댓값을 구하는 것이기 때문에
        # res라는 변수를 별도로 만들어주어 target이 arr[mid]값보다 클 경우 res = mid 세팅하여 위치 최댓값을 저장.
        mid = (l+r) // 2
        if B[mid] < num:
            l = mid + 1
            res = mid
        else:
            r = mid - 1

    return res

T = int(read())

A=[]
B=[]
for i in range(T):
    n,m = map(int,read().split())
    A = list(map(int , read().split()))
    B = list(map(int , read().split()))
    A.sort()
    B.sort()

    tot_cnt = 0
    for j in A:
        tot_cnt += binary_search(j, m) + 1

    print(tot_cnt)
