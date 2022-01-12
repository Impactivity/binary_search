# 주어진 논문 n 편중 h번 이상 인용된 논문이 h편 이상일 때,
# Index-h 값은 h가 된다.
# 과학자가 논문의 인용 횟수를 담은 배열 citations가 주어짐.

citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations = sorted(citations)

    start = 0
    end = citations[-1]

    # 이분탐색으로 풀이
    while start <= end:
        mid = (start + end) // 2

        # mid 값보다 큰 대상들 카운트
        cnt = 0
        for num in citations:
            if num >= mid:
                cnt += 1

        # mid 값이 더 큰 경우에는 end 값을 감소시켜서 조정
        if mid > cnt:
            end = mid - 1
        # mid 값이 더 작은 경우에는 start 값을 증가시켜서 조정
        elif mid <= cnt:
            start = mid + 1

    return end

print(solution(citations))