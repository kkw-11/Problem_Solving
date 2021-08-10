import heapq

class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]
        # self.data = []

    def push(self, value) :
    
        # heapq.heappush(self.data, value)
        
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        # self.data[0] += 1
        
        child = len(self.data) -1
        parent = child // 2
        
        while child > 1:
            if self.data[parent] > self.data[child]:
                self.data[parent], self.data[child] = self.data[child], self.data[parent]
                
                child = parent
                parent = child // 2
            else:
                break

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
#         if len(self.data) == 0:
#             return
#         heapq.heappop(self.data)
        
        if len(self.data) == 1:
            return
        
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        self.data.pop()
        
        parent = 1 
        child = parent * 2
        
        while True:
            lastIndex = len(self.data) - 1
            
            if child > lastIndex:
                break
            elif child + 1 > lastIndex:
                pass
            else:
                if self.data[child] > self.data[child + 1]:
                    child = child + 1
            
            if self.data[parent] > self.data[child]:
                self.data[parent], self.data[child] = self.data[child] , self.data[parent]  
                parent = child
                child = parent * 2
            else:
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        
        if len(self.data) == 1:
            return -1
            
        return self.data[1]
