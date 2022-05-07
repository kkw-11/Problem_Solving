import sys
def choose(set_nums,start):
    global answers,n,m
    if len(set_nums) == m:
        answers.append(set_nums)
    else:
        for next in range(start+1,n+1):
            set_nums.append(next)
            choose(set_nums.copy(),next)
            set_nums.pop()

input = sys.stdin.readline
answers = []
n, m = map(int,input().split())

for start in range(1,n+1):
    set_nums = [start]
    choose(set_nums,start)

for answer in answers:
    for num in answer:
        print(num,end=" ")
    print()