import sys

def choose(set_nums):
    global answers,n,m
    if len(set_nums) == m:
        answers.append(set_nums)
    else:
        for i in range(1,n+1):
            if checked[i]:continue
            checked[i] = True
            set_nums.append(i)
            choose(set_nums.copy())
            checked[i] = False
            set_nums.remove(i)

input = sys.stdin.readline

n, m = map(int,input().split())

set_nums = []
checked = [False for _ in range(n+1)]
answers = []
choose(set_nums)

for answer in answers:
    for a in answer:
        print(a,end=" ")
    print()