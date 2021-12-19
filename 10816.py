from sys import stdin

N = int(input())
own_cards = sorted(map(int, stdin.readline().split()))
M = int(input())
cardlist = map(int, stdin.readline().split())

def binary_serach(card,start,end):

    if start > end:
        return 0

    mid = (start+end) // 2

    if card == own_cards[mid]:
        return own_cards[start:end+1].count(card)
    elif card < own_cards[mid]:
        return binary_serach(card,start,mid-1)
    else :
        return binary_serach(card,mid+1 , end)


dic = {}

for card in own_cards:
    start = 0
    end = N-1
    if card not in dic :
        dic[card] = binary_serach(card,start,end)


print( ' '.join(str(dic[m]) if m in dic else '0' for m in cardlist ))
