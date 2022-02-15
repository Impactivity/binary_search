import sys
read= sys.stdin.readline

def binary_search(num):
    l = 0
    r = len(card)-1

    while l <= r:
        mid = (l+r) // 2

        if card[mid] == num:
            return 1
        elif card[mid] < num:
            l = mid + 1
        else:
            r = mid - 1

    return 0

n = int(read()) # 1 <= n <= 500,000
card = list(map(int,read().split()))
card.sort()
m = int(read()) # 1<= m <= 500,000
numbers = list(map(int,read().split()))

# 주어진 numbers들이 card에 있는 숫자인지 binary search로 확인
# 이중 for 문으로 구현하면 최대 500,000 * 500,000 번의 연산이 필요하므로 (시간복잡도 : o(n**2) )
# 이진탐색 (시간복잡도 : o( log(n)) 을 이용하여 확인한다.
for num in numbers:
    answer = binary_search(num)
    print(answer , end = ' ')

