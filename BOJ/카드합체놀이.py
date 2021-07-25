import sys
import heapq

#sys.stdin = open("input.txt","rt")

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0

heapq.heapify(cards)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1+card2)
    heapq.heappush(cards, card1+card2)

for i in range(n):
    res += heapq.heappop(cards)

print(res)
