import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    number_of_docs, target = map(int,input().split())
    docs = list(map(int,input().split()))

    print_q = deque()

    for index, value in enumerate(docs):
        print_q.append((index,value))

    cnt = 1

    while print_q:
        front_doc = print_q.popleft()

        for cur_doc in print_q:
            if cur_doc[1] > front_doc[1]:
                print_q.append(front_doc)
                break
        else:
            if front_doc[0] == target:
                print(cnt)
                break
            else:
                cnt += 1