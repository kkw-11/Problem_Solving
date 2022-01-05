# 우선순위 큐 정렬로 해결
def solution(numbers):
    answer = ""
    data = [0]
    
    def push(value) :
    
        data.append(value)
        
        child = len(data) -1
        parent = child // 2
        
        while child > 1:
            if int(data[parent] + data[child]) < int(data[child] + data[parent]):
                data[parent], data[child] = data[child], data[parent]
                
                child = parent
                parent = child // 2
            else:
                break

    def pop() :
        nonlocal answer 

        if len(data) == 1:
            return

        data[1], data[-1] = data[-1], data[1]
        answer += data.pop()

        parent = 1 
        child = parent * 2

        while True:
            lastIndex = len(data) - 1

            if child > lastIndex: #자식이 없는경우
                break
            elif child + 1 > lastIndex: # 왼쪽 자식만 있는경우
                pass
            else:
                if int(data[child] + data[child + 1]) >  int(data[child + 1] + data[child]):
                    child = child
                else:
                    child = child +1

            if int(data[parent] + data[child]) < int(data[child] + data[parent]):
                data[parent], data[child] = data[child], data[parent]  
                parent = child
                child = parent * 2
            else:
                break

    numbers_str = list(map(str,numbers))

    for number in numbers_str:
        push(number)
    for _ in range(len(data)-1):
        pop()

        
    return str(int(answer))
    
