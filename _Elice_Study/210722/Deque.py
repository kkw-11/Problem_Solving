# pushFront, pushRear, popFront, popRear
class Deque():
    def __init__(self):
        self.data = []

    def addFront(self,data):
        self.data.insert(0,data)
    
    def addRear(self, data):
        self.data.append(data)

    def popFront(self):
        if len(self.data) == 0:
            return 
        return self.data.pop(0)

    def popRear(self):
        if len(self.data) == 0:
            return

        return self.data.pop()

pq = Deque()    

pq.addFront(1)
pq.addFront(2)
pq.addFront(3)

print(pq.data)

print(pq.popFront())
