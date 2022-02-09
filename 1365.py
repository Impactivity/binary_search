import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int,read().split()))


def binary_search(line, num):
    l = 0
    r = len(line)-1

    while l < r:
        mid = (l+r) // 2
        print(l,r)
        #비교하려는 숫자가 List[mid] 값보다 큰 경우는
        # l 에 mid+1 를 해준다,
        if line[mid] < num:
            l = mid + 1
        else: # 그렇지 않으면 r은 mid가 되는데
            r = mid
    return r

answer = []
answer.append(arr[0])

for i in range(1,n) :
    if answer[-1] < arr[i]:
        answer.append(arr[i])
    else:
        pos = binary_search(answer,arr[i])
        answer[pos] = arr[i]


print(n-len(answer))







