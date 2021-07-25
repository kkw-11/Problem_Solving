n = int(input())
s = []
cmd = []
count = 1
flag = True
for i in range(n):
    num = int(input())

    while count <= num:
        s.append(count)
        cmd.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        cmd.append('-')
    # [3, 1, 2, 4]
    else: 
        flag = False
        
if flag == False:
    print('NO')
else:
    for i in cmd:
        print(i)