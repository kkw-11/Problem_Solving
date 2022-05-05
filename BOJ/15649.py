import sys

def choose(set_nums):
    global answers,n,m
    if len(set_nums) == m:
        answers.append(set_nums)
    else:
        for i in range(1,n+1):
            if i in set_nums:continue
            set_nums.append(i)
            choose(set_nums.copy())
            set_nums.remove(i)

input = sys.stdin.readline

n, m = map(int,input().split())

set_nums = []

answers = []
choose(set_nums)
answers.sort()

for answer in answers:
    for a in answer:
        print(a,end=" ")
    print()