import sys

def find():
    global n
    dis = -1
    for row in range(n):
        for col in range(n):
            cnt1 = 1
            for i in range(1,n-col):
                if table[row][col] == table[row][col+i]:
                    cnt1 += 1
                else:
                    break
            cnt2 = 1
            for i in range(1,n-row):
                if table[row][col] == table[row+i][col]:
                    cnt2 += 1
                else:
                    break
            dis = max(dis,cnt1,cnt2)

    return dis

sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
table = [[] for _ in range(n)]
max_dis = -1

for row in range(n):
    input_data = input().rstrip()
    table[row].extend(list(input_data))

for row in range(n-1):
    for col in range(n-1):
        if table[row][col] != table[row][col+1]:
            table[row][col], table[row][col+1] = table[row][col+1], table[row][col]
            max_dis = max(find(),max_dis)
            table[row][col], table[row][col+1] = table[row][col+1], table[row][col]

        if table[row][col] != table[row+1][col]:
            table[row][col], table[row+1][col] = table[row+1][col], table[row][col]
            max_dis = max(find(),max_dis)
            table[row][col], table[row+1][col] = table[row+1][col], table[row][col]

for col in range(n-1):
    if table[n-1][col] != table[n-1][col+1]:
        table[n-1][col], table[n-1][col+1] = table[n-1][col+1], table[n-1][col]
        max_dis = max(find(),max_dis)
        table[n-1][col], table[n-1][col+1] = table[n-1][col+1], table[n-1][col]
    
for row in range(n-1):
    if table[row][n-1] != table[row+1][n-1]:
        table[row][n-1], table[row+1][n-1] = table[row+1][n-1], table[row][n-1]
        max_dis = max(find(),max_dis)
        table[row][n-1], table[row+1][n-1] = table[row+1][n-1], table[row][n-1]

print(max_dis)
