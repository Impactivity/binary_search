from sys import stdin

read = stdin.readline

N,C = map(int, read().split())

house_pos = sorted([int(read()) for _ in range(N) ])

# 가장 인접한 공유기 거리가 최댓값인 간격을 구하는 문제
# 0번째집에 설치했다고 가정하면
# 간격은 최소 1일것이기 때문에 start = 1

start = 1
end = house_pos[N-1] - house_pos[0]

def binary_search(start,end ):
    while start <= end:
        count = 1
        mid = (start + end) // 2
        current_house = house_pos[0] #처음 공유기 위치는 항상 첫 집이 되어야함.

        for i in range(1, N):
            if house_pos[i] > mid + current_house:
                count += 1
                current_house = house_pos[i]

        # 적게 놓을 수록 간격 커지기때문에
        # 공유기 간 간격 최댓값을 구하려면,
        # 현재 count가 놓아야하는 수보다 크거나 같을 때 (count수가 많다는 것은 현재 간격이 작다는 것)간격기준을 올리면
        # 최댓값을 구할 수 있지 않을까
        # count가 적다는 것은 공유기 간격을 좁혀도 된다는 뜻이다.

        if count < C:
            end = mid - 1
        else :
            start = mid + 1
    print(mid)

binary_search(start,end)