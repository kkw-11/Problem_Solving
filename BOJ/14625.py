import sys 

input = sys.stdin.readline

start_h, start_m = map(int,input().split())
end_h, end_m = map(int,input().split())
n = int(input())
cnt = 0
cur_h = start_h
cur_m = start_m
while True:

    if cur_m % 10 == n or cur_m // 10 == n or cur_h % 10 == n or cur_h // 10 == n:
        cnt += 1

    if cur_h ==  end_h and cur_m == end_m:
        break
    cur_m += 1
    if cur_m == 60:
        cur_m = 0
        cur_h += 1

print(cnt)