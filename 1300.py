# 문제
# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다.
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다.
# B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 배열 A와 B의 인덱스는 1부터 시작한다.

N = int(input())
k = int(input())

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2

        cnt = 0

        # 어떤 수가 몇번째 위치한 숫자인지 알려면 해당 숫자보다 작은 수가 몇 개가 존재하는지 알면 되는데
        # n*n 행렬에서 어떤 수 보다 작은 수가 몇 개 인지 아는 방법은 각 행에서 해당 수보다 작거나 같은 수를 모두 더해주면 된다.
        # 즉,1행을 보면  1*1, 1*2 , 1*3 ... 이런식으로 증가하는데 예를들어 3*3행렬에서 첫번째행에 4라는 수보다 작거나 같은 수는 3개임을 알 수 있다.
        # 수식으로 나타내면 1이 공통으로 곱해지기 떄문에 4 // 1 이지만 3*3 행렬에서 4가 나올 수 없기 떄문에 정답은 3이다.
        # n*n 행렬에서 즉, min( 해당수 // 행 , N) 이 될 것이다.
        #
        for i in range(1, N+1): #1행부터 n행까지
            cnt += min( mid // i , N)

        if cnt < target:
            start = mid + 1
        else :
            end = mid - 1

    return start

print( binary_search(1,N*N,k))