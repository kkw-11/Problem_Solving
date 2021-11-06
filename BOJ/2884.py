import sys

input = sys.stdin.readline

hour, minute = map(int,input().split())

if minute>=45:
    print(hour, minute - 45)
else:
    if hour == 0:
        print(23,60+minute - 45)
    else:
        print(hour-1, 60+minute-45)