import sys
#sys.stdin = open("input.txt","rt")

card = list(range(21))

for _ in range(10):
    a, b = map(int,input().split())
    for i in range((b-a+1)//2):
        card[a+i], card[b-i] = card[b-i], card[a+i]

card.pop(0)

for x in card:
    print(x,end=" ")