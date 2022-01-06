import sys
input = sys.stdin.readline
points = []
x_dict = {}
y_dict = {}
answer = []
for _ in range(3):
    x, y = input().split()
    if not x in x_dict:
        x_dict[x] = 1
    else:
        x_dict[x] += 1

    if not y in y_dict:
        y_dict[y] = 1
    else:
        y_dict[y] += 1

for key, value in x_dict.items():
    if value == 1:
        answer.append(key)
for key, value in y_dict.items():
    if value == 1:
        answer.append(key)
print(*answer)