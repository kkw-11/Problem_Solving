import sys

input_data = sys.stdin.readline().rstrip()
cnt = [0] * 26
maxCnt = 0
idx = list()

for elem in input_data:
    ascii = ord(elem)

    if ascii >= 65 and ascii <= 90:
        cnt[ascii - 65] += 1
    elif ascii >= 97 and ascii <=122:
        cnt[ascii - 97] += 1

maxCnt = max(cnt)

for i in range(len(cnt)):
    if maxCnt == cnt[i]:
        idx.append(i)

if len(idx) == 1:
    print(chr(idx[0]+65))
elif len(idx) > 1:
    print("?")
