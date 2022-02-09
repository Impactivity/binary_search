#프로그래머스 징검다리 문제
# distance = 25
# rocks =[2, 14, 11, 21, 17]
# n = 2

def solution(distance, rocks, n):
    rocks.sort()

    l = 1  # 돌 사이에 최소값은 1이다.
    r = distance

    while l <= r:
        # mid값이 n개의 돌을 제거했을 때 돌사이 거리 최소값이라고 가정.
        mid = (l + r) // 2

        del_stone = 0
        pre_stone = 0

        for num in rocks:
            # mid 값이 최솟값이기 때문에 현재 돌은 제거해야한다.
            if num - pre_stone < mid:
                del_stone += 1
            else:
                pre_stone = num

        # 제거해야할 갯수보다 많다는 것은 mid 값이 너무 크다는 것이다.
        # 따라서 r값을 조정한다.
        if del_stone > n:
            r = mid - 1
        else:
            l = mid + 1

    return r