import sys

read = sys.stdin.readline

n = int(read()) # 1 <= n <= 100,000

# case 1
# 2 a b , (2 : 사탕을 넣음 , a : 사탕의 맛정도 ( 1 ~ 1,000,000 ) , c : 사탕갯수 ( c <0 이면 사탕을 뺀다.)
# 1 c  ( 1 : 사탕을 뺀다, c : 사탕의 순위 )

cases = [list(map(int, read().split())) for _ in range(n)]

cases.sort(reverse = True)

# 0. 앞자리가 2인 대상인 마지막 inx 를 이분탐색으로 탐색
# 1. 사탕 갯수 파악
# 2. 맛 순위에 따라 candies 배열에 사탕 갯수 cnt 입력
# 3. 앞자리가 1인 대상부터 차례로 사탕 빼서 출력

print(cases)