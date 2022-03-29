import sys

read = sys.stdin.readline

T = int(read())

for i in range(T):
    N = int(read())
    note_1 = sorted(list(map(int, read().split())))
    M = int(read())
    note_2 = list(map(int,read().split()))
    #note2 에 있는 숫자가 note1에 있는지 판별
    for num in note_2:
        l = 0
        r = N-1
        isTrue = False
        while l <= r:
            mid = (l+r) // 2

            if num < note_1[mid]:
                r = mid - 1
            elif num > note_1[mid]:
                l = mid + 1
            else:
                isTrue = True
                break

        if isTrue == False:
            print(0)
        else:
            print(1)


