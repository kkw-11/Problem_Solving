import sys

input = sys.stdin.readline

number_of_vilages = int(input())
costs = list(map(int,input().split()))

max_cost = float("-inf")
start = 1
for vilage, cost in enumerate(costs):
    if max_cost < cost:
        start = vilage
        max_cost = cost
total_cost = 0
for move_cnt in range(number_of_vilages-1):
    total_cost += costs[(start+1+move_cnt)%number_of_vilages]

print(total_cost)
