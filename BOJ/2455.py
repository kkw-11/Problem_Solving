import sys

input = sys.stdin.readline

max_total = 0
total = 0
for _ in range(4):
    get_in, get_off = map(int,input().split())
    total -= get_in
    total += get_off

    if total > max_total:
        max_total = total

print(max_total)
