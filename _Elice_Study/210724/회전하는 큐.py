from collections import deque 
n,m = list(map(int,input().split())) 
value = list(map(int,input().split())) 
q = deque([i+1 for i in range(n)]) 
count = 0 

for x in value: 
    while True: 
        if q.index(x) == 0: 
            q.popleft() # 1번 로직 
            break 
        # 위치 0과의 거리 차이로 왼쪽으로 이동할 지 오른쪽으로 이동할 지를 결정 
        if q.index(x) - 0 <= len(q) - q.index(x): 
                # 2번 왼쪽으로 이동하기 로직 
            q.append(q.popleft()) 
            count += 1 
        else: 
            q.appendleft(q.pop()) # 3번 오른쪽으로 이동하기 로직 
            count += 1 
            print(count)
