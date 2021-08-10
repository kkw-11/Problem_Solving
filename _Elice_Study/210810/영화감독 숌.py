n = int(input())

# 순번 
count = 0
# 제목
result = 666

while 1:
    # 666이 존재하면 순번 +1
    if '666' in str(result):
        count += 1
    # 순번이 원하는 순번 n과 같다면 출력 후 break
    if count == n:
        print(result)
        break
    # 제목에 +1
    result += 1