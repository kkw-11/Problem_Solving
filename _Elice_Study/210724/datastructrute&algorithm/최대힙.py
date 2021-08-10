import heapq

class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다.
    '''
    
    def __init__(self) :
        self.data = []

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heapq.heappush(self.data, -value)

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''

        if len(self.data) == 0:
            return -1
        
        return -self.data[0]
        
