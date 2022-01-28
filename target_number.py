from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    #양수, 음수 값을 queue에 적재
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    le = len(numbers)

    while queue:
        n, i = queue.popleft()

        # 현재 i 값이 numbers의 마지막 인덱스랑 같고
        # 총합이 target과 같을 때
        if n == target and i == le - 1:
            answer += 1

        # 적재할 값이 더 남았을 경우
        if i + 1 < le:
            queue.append((n + numbers[i + 1], i + 1))
            queue.append((n - numbers[i + 1], i + 1))

    return answer


# solution 2 dfs 풀이

# s = []
# cnt = 0
#
# def dfs(_sum, depth, numbers, target):
#     global cnt
#
#     if depth == len(numbers):
#         if _sum == target:
#             cnt += 1
#             return
#         return
#
#     dfs(_sum + numbers[depth], depth + 1, numbers, target)
#     dfs(_sum - numbers[depth], depth + 1, numbers, target)
#     return
#
#
# def solution(numbers, target):
#     dfs(0, 0, numbers, target)
#     return cnt