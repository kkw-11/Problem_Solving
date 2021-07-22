import sys

#sys.stdin = open("input.txt","rt")

N = int(sys.stdin.readline())
stack = [None]* 100001
top = -1

def Push(data):
    global top
    global stack
    top += 1
    stack[top] = data

def Pop():
    global top
    global stack

    if top == -1:
        print(-1)
    else:
        print(stack[top])
        top -= 1

def Size():
    global top
    global stack

    print(top + 1)

def Empty():
    global top
    if top == -1:
        print(1)
    else:
        print(0)

def Top():
    global top
    global stack
    if top == -1:
        print(-1)
    else:
        print(stack[top])


for _ in range(N):
    # cmd = sys.stdin.readline().rstrip().split(" ")
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        Push(cmd[1])
    elif cmd[0] == "pop":
        Pop()
    elif cmd[0] == "size":
        Size()
    elif cmd[0] == "empty":
        Empty()
    elif cmd[0] == "top":
        Top()