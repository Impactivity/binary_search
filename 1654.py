################################################################
# 주어진 K개의 랜선 잘라서 N개의 랜선을 만들려고 하는데
# 자르는 높이의 최댓값을 구하는 문제
# 1 <= K <= 10000 정수, 1 <= N <= 1000000 정수 ,  항상 K <= N 이다.
# 랜선(lines)의 길이는 2**31 - 1 보다 작거나 같은 자연수
################################################################

import sys
read = sys.stdin.readline

K, N = map(int, read().split())

lines = [ int(read()) for _ in range(K)]

lines.sort()
start = 1
end = lines[K-1]

def binary_search(start,end):
    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in lines:
            count += ( i // mid ) #mid길이로 잘랐을 때 나오는 랜선 갯수의 합
        if count >= N: # count가 주어진 목표 N개보다 많다는 것은 작게 잘랐다는 뜻.
            # 같은 경우에도 더 크게 잘라서 최대값이 나오도록 한다.
            start = mid + 1 # start의 위치를 증가시켜주면 잘라지는 크기가 커질 것이기 때문에 count수는 자연스럽게 줄어들 것.
        else:
            end = mid - 1
    print(end)


binary_search(start,end)


